<template>
  <NavPage
    :username="username"
    :users="users"
    :score="score.toString()"
    :header="'Угадай мелодию'"
  >
    <template v-if="judge!==username" #debug>
      Player debugger
      <v-btn v-for="state in states.Player"
             @click="stateSwitcher(state)"
             :key="state"
             :disabled="state===$data.state"
      >{{ state }}
      </v-btn>
    </template>
    <template>

      <template v-if="state===states.Player.STARTING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ожидание начала
              игры</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Player.READY">
        <v-row align="center"
               justify="center" class="align-self-start">
          <BigFab @click="answerBtnHandler" text="Ответить"/>
        </v-row>
      </template>

      <template v-if="state===states.Player.ANSWERING">
        <TextField>
          <template #default>
            <v-text-field
              autofocus
              clearable
              :height="100"
              solo
              label="Ответ"
              v-model="givenAnswer"
            />
          </template>
          <template #button>
            <SmallFab @click="submitAnswerBtnHandler" type="forward"/>
          </template>
        </TextField>
      </template>

      <template v-if="state===states.Player.ANSWERED">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="artist" :track="track" :turned="answerIsCorrect!==undefined"/>
        </v-row>
      </template>

      <template v-if="state===states.Player.WAITING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              ответа ¯\_(ツ)_/¯</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Player.WAITED">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="'#ffcc00'" :artist="artist" :track="track" :turned="answerIsCorrect!==undefined"/>
        </v-row>
      </template>


    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";
import FlipCard from "@/components/FlipCard";
import WS from "@/views/Games/Game/Shared/ws";

export default {
  name: "Player",
  components: {FlipCard, TextField, SmallFab, BigFab, NavPage},
  data: () => ({
    username: '',
    users: [],
    sessionId: '',

    judge: '',
    started: false,

    score: 100,

    state: 'p_starting',
    states: {
      Player: {
        STARTING: "p_starting",
        READY: "p_ready",
        ANSWERING: "p_answering",
        ANSWERED: "p_answered",
        WAITING: "p_waiting",
        WAITED: "p_waited"
      }
    },
    // p_starting, p_ready, p_answering, p_answered, p_waiting, p_waited

    answerIsCorrect: undefined,
    givenAnswer: 'пошлая молли',
    track: 'Новый мерин',
    artist: 'Моргенштерн',
  }),
  methods: {
    setState(state) {
      this.state = state;
    },
    setAnswerIsCorrect(value) {
      this.track = 'Новый мерин'; //todo: remove
      this.artist = 'Моргенштерн'; //todo: remove

      this.answerIsCorrect = value;
    },

    stateSwitcher(state) {
      switch (state) {
        case this.states.Player.STARTING:
          this.playerToStarting();
          break;
        case this.states.Player.READY:
          this.playerToReady();
          break;
        case this.states.Player.ANSWERING:
          this.playerToAnswering();
          break;
        case this.states.Player.ANSWERED:
          this.playerToAnswered();
          break;
        case this.states.Player.WAITING:
          this.playerToWaiting();
          break;
        case this.states.Player.WAITED:
          this.playerToWaited();
          break;
      }
    },

    //p_starting
    playerToStarting() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState(this.states.Player.STARTING);
    },

    //p_ready
    playerToReady() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState(this.states.Player.READY);
    },
    async answerBtnHandler() {
      // check if he was fast enough, instead of true
      const answering = true; // todo: handle

      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"event": "answer"}
      };
      await WS.socket.send(JSON.stringify(data_json));

      if (answering) {
        // todo: handle state change inside listener
        this.setState(this.states.Player.ANSWERING);
      } else {
        this.setState(this.states.Player.WAITING);
      }
    },

    //p_answering
    playerToAnswering() {
      this.setState(this.states.Player.ANSWERING);
    },
    async submitAnswerBtnHandler() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer": this.givenAnswer}
      };
      await WS.socket.send(JSON.stringify(data_json));
      this.givenAnswer = "";

      // this.answerIsCorrect = true;
      const answerCorrect = true; // todo: handle to commented above var

      if (answerCorrect) {
        this.setState(this.states.Player.ANSWERED);
        setTimeout(this.setAnswerIsCorrect, 3000, true); // todo: handle
      }
    },

    //p_answered
    playerToAnswered() {
      this.setState(this.states.Player.ANSWERED);
    },


    //p_waiting
    playerToWaiting() {
      this.setState(this.states.Player.WAITING);
    },

    //p_waited
    playerToWaited() {
      this.setState(this.states.Player.WAITED);
      setTimeout(this.setAnswerIsCorrect, 3000, true); // todo: replace true (stub)
    },

  },
}
</script>