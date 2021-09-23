import json
from typing import MutableMapping, List
from fastapi import WebSocket
from game_engine import GameEngine
import logging

logger = logging.getLogger(__name__)


class GameSession:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.active_connections: MutableMapping[str, WebSocket] = {}
        self.host = None
        self.desktop = None
        self.current_game = GameEngine(self)

    def should_connect_desktop(self):
        return self.desktop is None

    def connect_desktop(self, websocket):
        self.desktop = websocket

    def disconnect_desktop(self):
        self.desktop = None

    def should_connect(self, token: str):
        return token not in self.active_connections and self.current_game.allow_connect(token)

    def connect(self, token: str, websocket: WebSocket):
        self.active_connections[token] = websocket
        if self.host is None:
            self.host = token
        self.current_game.add_player(token)

    async def disconnect(self, token: str):
        self.active_connections.pop(token, None)
        if self.host == token:
            if len(self.active_connections) == 0:
                self.host = None
            else:
                self.host = next(iter(self.active_connections.keys()))
        await self.current_game.disconnect_player(token)

    async def game_update(self, token: str, data):
        await self.current_game.update(token, data)

    async def send_personal_message(self, token: str, data):
        try:
            await self.active_connections[token].send_json(json.dumps(data))
        except TypeError:
            logger.error(str(data))
            exit(-1)

    async def send_desktop(self, data):
        if self.desktop is not None:
            try:
                await self.desktop.send_json(json.dumps(data))
            except TypeError:
                logger.error(str(data))
                exit(-1)

    async def broadcast(self, data, block: List[str] = None):
        if block is None:
            block = []
        for token, connection in self.active_connections.items():
            if token in block:
                continue
            try:
                await connection.send_json(json.dumps(data))
            except TypeError:
                logger.error(str(data))
                exit(-1)
