<template>
  <div class="main-wrapper">
    <template
      v-if="currentState===states.Game.CREATE || currentState===states.Game.LOGIN || currentState===states.Game.ROLE"
    >
      <NavPage :header="currentState===states.Game.LOGIN? 'Логин': 'Угадай мелодию'"
               :username="username"
               :users="users"
               :judge="judge"
      >
        <template v-if="currentState===states.Game.CREATE">
          <v-row align="center"
                 justify="center" class="align-self-start">
            <template v-if="loading">
              <v-progress-circular
                :size="70"
                :width="7"
                color="#ffcc00"
                indeterminate
              ></v-progress-circular>
            </template>
            <template v-else>
              <v-col cols="11" sm="10" md="10" lg="7" xl="7">
                <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Отсканируйте
                  с
                  вашего
                  смартфона чтобы начать</h3>
                <v-row justify="center" align="center" no-gutters>
                  <QRCode
                    :value="qrcodeValue"
                    :copyOnClick="true"
                  />
                </v-row>
              </v-col>
            </template>
          </v-row>
        </template>
        <template v-else-if="currentState===states.Game.LOGIN">
          <TextField>
            <template #default>
              <v-text-field
                autofocus
                clearable
                :counter="10"
                :height="100"
                solo
                v-model="username"
                :placeholder="'Никнейм'"
                :maxlength="10"
                :error="loginError"
                :error-messages="loginError?'Логин не должен быть пустым':''"
                @keydown.enter="loginHandler"
              />
            </template>
            <template #button>
              <SmallFab @click="loginHandler" type="forward"/>
            </template>
          </TextField>
        </template>
        <template v-else-if="currentState===states.Game.ROLE">
          <v-row align="center"
                 justify="center" class="align-self-start">
            <v-spacer/>
            <BigFab @click="playerChoiceHandler" text="Стать игроком"/>
            <v-spacer/>
            <BigFab @click="judgeChoiceHandler" text="Стать ведущим" :active="!judge" :color="'#FFCC00'"/>
            <v-spacer/>
          </v-row>
        </template>
      </NavPage>
    </template>
    <template v-else-if="currentState===states.Game.PLAYING">
      <template v-if="host">
        <NavPage :header="'Угадай мелодию'" :users="users" :judge="judge" :username="'Главный экран'">
          <v-row align="center"
                 justify="center" class="align-self-start">
            <v-col align="center">
              <MusicPlayer :rotating="musicIsPlaying" :counter="counter"/>
            </v-col>
          </v-row>
        </NavPage>
      </template>
      <Player v-else-if="judge!==username"
              :username="username"
              :users="users"
              :sessionId="sessionId"
              :judge="judge"
              :state="playerState"
              :WS="WS"
              :answering-player="answeringPlayer"
              :song="song"
              :answerIsCorrect="answerIsCorrect"
              :given-answer="givenAnswer"
              :score="score"
              @changeState="setPlayerState"
      />
      <Judge v-else
             :username="username"
             :users="users"
             :sessionId="sessionId"
             :judge="judge"
             :state="judgeState"
             :WS="WS"
             :answering-player="answeringPlayer"
             :song="song"
             :answerIsCorrect="answerIsCorrect"
             :given-answer="givenAnswer"
             @changeState="setJudgeState"
      />
    </template>
    <template v-else-if="currentState===states.Game.SCOREBOARD">
      <LeaderBoard :scoreboard="scoreboard" :username="username"/>
    </template>
  </div>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";
import BigFab from "@/components/BigFab";
import QRCode from "@/components/QRCode";

import server from "@/data/hosts";
import States from "@/views/Games/Game/Shared/States";

import Player from "@/views/Games/Game/Player";
import Judge from "@/views/Games/Game/Judge";
import LeaderBoard from "@/views/Games/Game/LeaderBoard";
import MusicPlayer from "@/components/MusicPlayer";

export default {
  name: "GuessTheMelody",
  components: {
    MusicPlayer,
    LeaderBoard,
    Judge,
    Player,
    TextField,
    SmallFab,
    NavPage,
    BigFab,
    QRCode,
  },
  data: () => ({
    states: States,
    currentState: States.Game.CREATE,
    sessionId: "",
    username: "",
    users: [],
    judge: "",
    WS: undefined,
    answeringPlayer: "",
    givenAnswer: "",

    // create
    btnPressed: false,
    qrcodeValue: "не ну а че)",
    sessionURL: '',
    loading: true,

    // host (desktop)
    host: false,
    musicIsPlaying: false,
    counter: "",
    songAudio: undefined,

    // login
    loginError: false,

    // player
    playerState: States.Player.STARTING,
    score: "",

    // judge
    judgeState: States.Judge.STARTING,

    // song
    song: {},
    answerIsCorrect: undefined,

    started: false,
    scoreboard: undefined,
  }),
  methods: {
    // COMMON
    userConnected(user) {
      console.log("USER CONNECTED: " + "'" + user + "'");
      let temp_users = this.users;
      temp_users.push(user);
      this.users = temp_users;
    },
    userDisconnected(user) {
      console.log("USER DISCONNECTED: " + "'" + user + "'");
      let temp_users = this.users;
      temp_users.splice(temp_users.indexOf(user), 1);

      this.users = temp_users;

      if (this.judge === user) {
        this.setJudge('');
      }
    },

    // ROLE


    // SETTERS
    // todo: replace all assignments with setters
    setJudge(user) {
      if (user) {
        console.log("USER '" + user + "' IS JUDGE");
      } else {
        console.log("NO JUDGE");
      }

      this.judge = user;
    },
    setUsers(users) {
      this.users = users;
    },
    setState(state) {
      this.currentState = state;
    },
    setPlayerState(state) {
      this.playerState = state;
    },
    setJudgeState(state) {
      this.judgeState = state;
    },
    setAnswerIsCorrect(value) {
      this.answerIsCorrect = value;
    },
    setMusicIsPlaying(value) {
      this.musicIsPlaying = value;
      if (value) {
        this.songAudio.onended = () => {
          this.musicIsPlaying = false;
        }
        this.songAudio.play();
      } else {
        this.songAudio.pause();
      }
    },

    // HANDLERS

    // HANDLERS - LOGIN
    loginHandler() {
      if (!this.username.length) {
        this.loginError = true;
        return;
      } else {
        this.loginError = false;
      }

      this.WS = new WebSocket("ws://" + server.hostname + ":" + server.port + "/ws/" + this.sessionId + "/connect?token=" + this.username);

      this.WS.onerror = (error) => {
        console.error(error);
        this.$router.push('/games/guess-the-melody');
      };

      this.WS.onopen = () => {
        console.log('WebSocket opened');

        this.WS.onmessage = (data) => {
          this.serverMessagesHandler(data);
        }

        this.setState(States.Game.ROLE);
      };
    },

    // HANDLERS - ROLE
    playerChoiceHandler() {
      this.setState(States.Game.PLAYING);
    },
    async judgeChoiceHandler() {
      const judge_role_request_json = {"session_id": this.sessionId, "event_type": 2, "payload": {"update_role": true}};
      await this.WS.send(JSON.stringify(judge_role_request_json));

      this.setState(States.Game.PLAYING);
    },

    // HANDLERS - COMMON
    async sessionIdHandler(sessionId) {
      if (sessionId) {
        this.sessionId = sessionId;
        if (!this.host) {
          this.setState(States.Game.LOGIN);
        }
      } else {
        this.setState(States.Game.CREATE);
        const requestOptions = {
          method: "POST",
          headers: {"Content-Type": "application/json"},
        };
        const response = await fetch('http://' + server.hostname + ':' + server.port + '/session/create', requestOptions);
        console.log(response);
        const data = await response.json();
        console.log(data.session_id);
        this.sessionId = data.session_id;
        this.sessionURL = "/games/guess-the-melody/" + data.session_id;
        this.qrcodeValue = window.location.protocol + "//" + window.location.host + this.sessionURL;

        this.host = true;

        this.WS = new WebSocket("ws://" + server.hostname + ":" + server.port + "/ws/" + this.sessionId + "/desktop");

        this.WS.onerror = (error) => {
          console.error(error);
          this.$router.push('/games/guess-the-melody');
        };

        this.WS.onopen = () => {
          console.log('Desktop WebSocket opened');

          this.WS.onmessage = (data) => {
            this.serverMessagesHandler(data);
          }
        };
        this.loading = false;
      }
    },
    serverMessagesHandler(data) {
      let response;
      try {
        response = JSON.parse(JSON.parse(data.data));
        console.log();
        if (typeof response == "string") {
          console.warn("JSON is string");
        }
        console.log('Received json:');
        console.log(response);
      } catch (e) {
        console.warn(e);
        response = data.data;
        console.log('Received: ', response);
        return
      }

      let status = response['response_status'];
      let payload = response['payload'];


      switch (status) {
        case 1:
          if ("clients" in payload) {
            this.setUsers(payload.clients);
            if (payload.judge) this.setJudge(payload.judge);
          }
          break;
        case 2:

          break;
        case 3:
          if ("event" in payload) {
            switch (payload.event) {
              case "connected":
                this.userConnected(payload.client);
                break;
              case "disconnected":
                this.userDisconnected(payload.client);
                break;
            }
          } else if ("song" in payload && "answer" in payload && "answer_correct" in payload) {
            this.playerState = States.Player.WAITED;
            this.song = payload.song;
            this.givenAnswer = payload.answer;
            setTimeout(() => (this.answerIsCorrect = payload.answer_correct), 3000);
          } else if ("score_board" in payload) {
            this.scoreboard = payload.score_board.map((line) => ({username: line[0], score: line[1]}));
            this.scoreboard = this.scoreboard.filter((record) => (record.username !== this.judge));
            this.setState(States.Game.SCOREBOARD);
          }
          break;
        case 4:
          if ("event" in payload) {
            switch (payload.event) {
              case "judge":
                this.setJudge(payload.judge);
                break;
              case "play":

                this.answeringPlayer = "";
                this.givenAnswer = "";
                if (this.judge !== this.username && !this.started && !this.host) this.score = "0";
                this.song = {};
                this.answerIsCorrect = undefined;

                this.playerState = States.Player.READY;
                this.judgeState = States.Judge.READY;
                this.started = true;
                break;
              case "answer":
                if ("first" in payload) {
                  this.answeringPlayer = payload.first;
                  if (this.host) {
                    this.setMusicIsPlaying(false);
                  }
                  if (this.username === this.answeringPlayer) {
                    this.playerState = States.Player.ANSWERING;
                  } else {
                    this.playerState = States.Player.WAITING;
                  }
                  this.judgeState = States.Judge.ANSWERING;
                }
                break;
            }
          } else if ("answer_correct" in payload && "song" in payload && "answer" in payload && "score" in payload) {
            this.playerState = States.Player.ANSWERED;
            this.song = payload.song;
            this.givenAnswer = payload.answer;
            setTimeout(() => (this.score = payload.score.toString()), 3000);
            setTimeout(this.setAnswerIsCorrect, 3000, payload.answer_correct);
          } else if ("answer" in payload && "song" in payload) {
            this.givenAnswer = payload.answer;
            this.song = payload.song;
            this.judgeState = States.Judge.CHECKING;
            this.playerState = States.Player.WAITING;
            // todo: consider no-judge game mode
          } else if ("song64" in payload) {
            if (!this.started) {
              this.$router.push(this.sessionURL);
              this.setState(States.Game.PLAYING);
            }
            this.songAudio = new Audio("data:audio/mp3;base64," + payload.song64);
            this.counter = "3";
            setTimeout(() => (this.setMusicIsPlaying(true)), 3000);
            setTimeout(() => (this.counter = " "), 3000);
            setTimeout(() => (this.counter = "1"), 2000);
            setTimeout(() => (this.counter = "2"), 1000);
          }
          break;
      }
    },
  },
  watch: {
    '$route.params.sessionId': function (val) {
      this.sessionIdHandler(val);
    }
  },
  async mounted() {
    await this.sessionIdHandler(this.$route.params.sessionId);
  },
}
</script>

<style lang="scss" scoped>
.app {
  .main-wrapper {
    flex: 1 1 auto;
    max-width: 100%;
    position: relative;
  }


}
</style>