from typing import MutableMapping, Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, Query, status
from fastapi.responses import HTMLResponse, Response, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from game_session import GameSession
from game_engine import *

import uvicorn
import uuid
import psycopg2
from dotenv import load_dotenv
import os
import base64
import json

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    html = open('index.html').read()
    return HTMLResponse(html)


class ConnectionManager:
    def __init__(self):
        self.active_sessions: MutableMapping[str, GameSession] = {}

    def get_session(self, session_id):
        return self.active_sessions.get(session_id, None)

    def should_connect(self, session: str, token: str):
        if session not in self.active_sessions:
            return False

        return self.active_sessions[session].should_connect(token)

    async def game_update(self, session: str, token: str, data):
        await self.active_sessions[session].game_update(token, data)

    def create_session(self, session: str):
        self.active_sessions[session] = GameSession(session)

    async def connect(self, session_id: str, token: str, websocket: WebSocket):
        judge = self.active_sessions[session_id].current_game.judge
        await websocket.accept()

        resp = ServerResponse(session_id, ResponseStatus.INFO)
        resp.payload = {
            "event": "connected",
            "client": token
        }
        await manager.broadcast(session_id, resp.__dict__)
        await self.active_sessions[session_id].send_desktop(resp.__dict__)

        self.active_sessions[session_id].connect(token, websocket)

        tokens = list(self.active_sessions[session_id].active_connections.keys())
        resp = ServerResponse(session_id, ResponseStatus.ACCEPT)
        resp.payload = {
            "clients": tokens,
            "judge": judge if judge is not None else ""
        }

        await self.active_sessions[session_id].send_personal_message(token, resp.__dict__)

    async def disconnect(self, session: str, token: str):
        await self.active_sessions[session].disconnect(token)

        resp = ServerResponse(session, ResponseStatus.INFO)
        resp.payload = {
            "event": "disconnected",
            "client": token
        }
        await manager.broadcast(session, resp.__dict__)
        await self.active_sessions[session].send_desktop(resp.__dict__)

    def terminate_session(self, session: str):
        self.active_sessions.pop(session)

    async def broadcast(self, session: str, message):
        await self.active_sessions[session].broadcast(message)


manager = ConnectionManager()


async def get_token(
        websocket: WebSocket,
        token: Optional[str] = Query(None)
):
    if token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return token


@app.post("/token")
def connect():
    return {"token": "some y games"}


@app.websocket("/ws/{session_id}/desktop")
async def ws_desktop_endpoint(websocket: WebSocket, session_id: str):
    session = manager.get_session(session_id)
    if not session.should_connect_desktop():
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    await websocket.accept()
    session.connect_desktop(websocket)

    tokens = list(manager.active_sessions[session_id].active_connections.keys())
    judge = manager.active_sessions[session_id].current_game.judge
    resp = ServerResponse(session_id, ResponseStatus.ACCEPT)
    resp.payload = {
        "clients": tokens,
        "judge": judge if judge is not None else ""
    }

    await manager.active_sessions[session_id].send_desktop(resp.__dict__)

    try:
        while True:
            data = await websocket.receive_json()
            await session.game_update("", data)
            # await manager.broadcast(session_id, f"Client #{token} says: {data}")

    except WebSocketDisconnect:

        session.disconnect_desktop()

        await session.broadcast(f"Main screen left")


@app.websocket("/ws/{session_id}/connect")
async def websocket_endpoint(websocket: WebSocket, session_id: str,
                             token: str = Depends(get_token)):
    if not manager.should_connect(session_id, token):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    await manager.connect(session_id, token, websocket)
    try:
        while True:
            data = await websocket.receive_json()

            await manager.game_update(session_id, token, data)
            # await manager.broadcast(room_id, f"Client #{token} says: {data}")

    except WebSocketDisconnect:

        await manager.disconnect(session_id, token)


@app.post("/session/create")
async def create_session():
    session_id = str(uuid.uuid4().fields[-1])[:5]
    manager.create_session(session_id)

    return {"session_id": session_id}


@app.post("/room/create")
async def create_room():
    room_id = str(uuid.uuid4().fields[-1])[:5]
    us = os.getenv("DB_USER")
    passwd = os.getenv("DB_PASSWORD")
    try:
        connection = psycopg2.connect(user=us,
                                      password=passwd,
                                      host="rc1b-rwpletdw8uzpunn0.mdb.yandexcloud.net",
                                      port="6432",
                                      database="yandexparty")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO rooms (room_id) VALUES (%s)"""
        record_to_insert = (room_id,)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(error)

    finally:
        if connection:
            cursor.close()
            connection.close()

    return {"room_id": room_id}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
