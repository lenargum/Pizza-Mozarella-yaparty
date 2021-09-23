import random
import enum
from typing import MutableMapping
import json
import base64
import os
import logging

logger = logging.getLogger(__name__)

class GameEvent(enum.Enum):
    UNDEFINED = 0
    START = 1
    UPDATE = 2
    FINISH = 3


class ResponseStatus(enum.Enum):
    UNDEFINED = 0
    ACCEPT = 1
    REJECT = 2
    INFO = 3
    UPDATE = 4


class ServerResponse:
    def __init__(self, session_id: str, status: ResponseStatus):
        self.session_id = session_id
        self.response_status: ResponseStatus = status.value
        self.payload: MutableMapping[str, object] = {}


class GameState(enum.Enum):
    UNDEFINED = 0
    START = 1
    PLAYING = 2
    ANSWERING = 3
    JUDGE = 4
    WAIT = 5
    FINISH = 6

    def __int__(self):
        return self.value


class GameEngine:
    """
    @param: tokens    - list of players tokens
    self.num_players - # of players
    self.scores      - list of int scores
    self.players     - dict of player<->score mapping
    self.now_playing - song that is now playing 
    self.songs       - list of song names
    """

    def __init__(self, session):
        self.scores: MutableMapping[str, int] = {}
        self.session = session
        self.now_playing = None
        self.answer_player = None
        self.judge = None
        self.state: GameState = GameState.UNDEFINED
        self.songs = []

    def add_player(self, token):
        self.scores[token] = 0

    async def disconnect_player(self, token):
        if self.judge is not None and token == self.judge:
            self.judge = None
            if self.state == GameState.JUDGE:
                self.state = GameState.PLAYING
                self.answer_player = None
                response = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
                response.payload["event"] = "disconnect"
                await self.session.broadcast(response.__dict__)

        if (self.state == GameState.ANSWERING or self.state == GameState.JUDGE) and token == self.answer_player:
            self.state = GameState.PLAYING
            self.answer_player = None
            response = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
            response.payload["event"] = "disconnect"
            await self.session.broadcast(response.__dict__)

    def allow_connect(self, token):
        return self.state == GameState.UNDEFINED

    async def start(self):
        self.state = GameState.START
        with open('songs.json') as songs_json:
            self.songs = json.load(songs_json)
        await self.next()

    async def next(self):
        if len(self.songs) == 0:
            self.state = GameState.FINISH

            leader_board = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
            resp = ServerResponse(self.session.session_id, ResponseStatus.INFO)
            resp.payload["score_board"] = leader_board
            await self.session.send_desktop(resp.__dict__)
            await self.session.broadcast(resp.__dict__)
            return
        song_id = random.randint(0, len(self.songs) - 1)
        self.state = GameState.PLAYING
        self.now_playing = self.songs.pop(song_id)
        if os.path.isfile(self.now_playing['path']):
            with open(self.now_playing['path'], 'rb') as f:
                audio_encoded = base64.b64encode(f.read())  # read file into RAM and encode it
            res = str(audio_encoded)[2:-1]
            song_resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
            song_resp.payload["song64"] = res
            await self.session.send_desktop(song_resp.__dict__)
        else:
            logger.error("Can't send the song. File doesn't exist: " + self.now_playing['path'])
        resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
        resp.payload["event"] = "play"
        await self.session.broadcast(resp.__dict__)

    def has_judge(self):
        return self.judge is not None

    async def judge_answer(self, data):
        resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
        resp.payload["song"] = self.now_playing
        resp.payload["answer"] = data["payload"]["answer"]

        resp_all = ServerResponse(self.session.session_id, ResponseStatus.INFO)
        resp_all.payload["song"] = self.now_playing
        resp_all.payload["answer"] = data["payload"]["answer"]

        if self.judge is not None:
            if data["payload"]["answer_correct"]:
                self.scores[self.answer_player] += 100
                resp.payload["answer_correct"] = True
                resp_all.payload["answer_correct"] = True
            else:
                self.scores[self.answer_player] -= 100
                resp.payload["answer_correct"] = False
                resp_all.payload["answer_correct"] = False
        else:
            if self.now_playing["author"].lower().strip().find(data["payload"]["answer"].lower().strip()) > -1 or \
                    self.now_playing["name"].lower().strip().find(data["payload"]["answer"].lower().strip()) > -1:
                self.scores[self.answer_player] += 100
                resp.payload["answer_correct"] = True
                resp_all.payload["answer_correct"] = True
            else:
                self.scores[self.answer_player] -= 100
                resp.payload["answer_correct"] = False
                resp_all.payload["answer_correct"] = False

        resp.payload["score"] = self.scores[self.answer_player]
        await self.session.send_personal_message(self.answer_player, resp.__dict__)

        await self.session.broadcast(resp_all.__dict__, [self.answer_player, self.judge])

        self.state = GameState.WAIT
        self.answer_player = None
        next_resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
        next_resp.payload["event"] = "next"
        if self.judge is not None:
            await self.session.send_personal_message(self.judge, next_resp.__dict__)
        else:
            await self.session.send_personal_message(self.session.host, next_resp.__dict__)

    async def update(self, token, data):
        if self.state == GameState.UNDEFINED:
            if data["event_type"] == GameEvent.START.value:
                if self.judge is not None:
                    if token == self.judge:
                        await self.start()
                else:
                    if token == self.session.host:
                        await self.start()
            elif data["event_type"] == GameEvent.UPDATE.value:

                if "update_role" in data["payload"] and data["payload"]["update_role"]:
                    if not self.has_judge():
                        self.judge = token
                        resp = ServerResponse(self.session.session_id, ResponseStatus.ACCEPT)
                        await self.session.send_personal_message(token, resp.__dict__)

                        resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
                        resp.payload = {
                            "event": "judge",
                            "judge": token
                        }
                        await self.session.broadcast(resp.__dict__)
                        await self.session.send_desktop(resp.__dict__)

                    else:
                        resp = ServerResponse(self.session.session_id, ResponseStatus.REJECT)
                        resp.payload["message"] = "Judge was already chosen"
                        await self.session.send_personal_message(token, resp.__dict__)
            return
        if self.state == GameState.FINISH:
            return
        if self.state == GameState.ANSWERING:
            if token != self.answer_player:
                return
        elif self.state == GameState.WAIT:
            if "event" in data["payload"] and data["payload"]["event"] == "next":
                if self.judge is not None:
                    if token == self.judge:
                        await self.next()
                else:
                    if token == self.session.host:
                        await self.next()
            return
        elif self.state == GameState.JUDGE:
            if token == self.judge:
                if "answer_correct" in data["payload"]:
                    await self.judge_answer(data)
            return
        elif self.state == GameState.PLAYING:
            if token == self.judge:
                return
            if "event" in data["payload"] and data["payload"]["event"] == "answer":
                self.state = GameState.ANSWERING
                self.answer_player = token

                all_resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
                all_resp.payload = {
                    "event": "answer",
                    "first": self.answer_player
                }

                await self.session.broadcast(all_resp.__dict__)
                await self.session.send_desktop(all_resp.__dict__)
            return

        # TODO: send to frontend ask

        if "answer" in data["payload"]:
            if self.judge is not None:
                resp = ServerResponse(self.session.session_id, ResponseStatus.UPDATE)
                resp.payload["answer"] = data["payload"]["answer"].strip()
                resp.payload["song"] = self.now_playing
                await self.session.send_personal_message(self.judge, resp.__dict__)
                self.state = GameState.JUDGE
                return

            await self.judge_answer(data)
