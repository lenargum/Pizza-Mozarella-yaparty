<template>
  <NavPage
    :username="login"
    :users="users"
    :score="score.toString()"
    :header="'Угадай мелодию'"
  >
    <template #debug>
      <v-btn v-for="state in states"
             @click="stateSwitcher(state)"
             :key="state"
             :disabled="state===$data.state"
      >{{ state }}
      </v-btn>
    </template>
    <template>

      <template v-if="state==='starting'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ожидание начала
              игры</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state==='ready'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <BigFab @click="answerBtnHandler" text="Ответить"/>
        </v-row>
      </template>

      <template v-if="state==='answering'">
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

      <template v-if="state==='answered'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="artist" :track="track" :turned="answerIsCorrect!==undefined"/>
        </v-row>
      </template>

      <template v-if="state==='waiting'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              ответа ¯\_(ツ)_/¯</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state==='waited'">
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
import WS from "@/views/Game/Shared/ws";

export default {
  name: "Player",
  components: {FlipCard, TextField, SmallFab, BigFab, NavPage},
  data: () => ({
    login: '',
    users: [],
    sessionId: '',

    score: 100,

    state: 'starting',
    states: ["starting", "ready", "answering", "answered", "waiting", "waited"],
    // starting, ready, answering, answered, waiting, waited

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
        case "starting":
          this.toStarting();
          break;
        case "ready":
          this.toReady();
          break;
        case "answering":
          this.toAnswering();
          break;
        case "answered":
          this.toAnswered();
          break;
        case "waiting":
          this.toWaiting();
          break;
        case "waited":
          this.toWaited();
          break;
      }
    },

    //starting
    toStarting() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState("starting");
    },

    //ready
    toReady() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState("ready");
    },
    async answerBtnHandler() {
      // check if he was fast enough, instead of true
      const answering = true; // todo: handle

      const data_json = {
        "room_id": this.sessionId, "event_type": 2, "payload": {"event": "answer"}
      };
      await WS.socket.send(JSON.stringify(data_json));

      if (answering) {
        this.setState("answering");
      } else {
        this.setState("waiting");
      }
    },

    //answering
    toAnswering() {
      this.setState("answering");
    },
    async submitAnswerBtnHandler() {
      const data_json = {
        "room_id": this.sessionId, "event_type": 2, "payload": {"answer": this.givenAnswer}
      };
      await WS.socket.send(JSON.stringify(data_json));
      this.givenAnswer = "";

      // this.answerIsCorrect = true;
      const answerCorrect = true; // todo: handle to commented above var

      if (answerCorrect) {
        this.setState("answered");
        setTimeout(this.setAnswerIsCorrect, 3000, true); // todo: handle
      }
    },

    //answered
    toAnswered() {
      this.setState("answered");
    },


    //waiting
    toWaiting() {
      this.setState("waiting");
    },

    //waited
    toWaited() {
      this.setState("waited");
      setTimeout(this.setAnswerIsCorrect, 3000, true); // todo: replace true (stub)
    },

  },
  mounted() {
    if (Object.keys(WS).length) {
      this.sessionId = WS.session;
      this.login = WS.login;
    } else {
      this.$router.go(-1);
    }
  },
  watch: {}
}
</script>

<style scoped>

</style>