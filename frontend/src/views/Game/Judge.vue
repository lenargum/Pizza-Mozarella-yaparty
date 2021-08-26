<template>
  <NavPage
    :username="login"
    :users="users"
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
          <BigFab @click="startBtnHandler" text="Начать игру"/>
        </v-row>
      </template>

      <template v-if="state==='ready'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              самого быстрого...</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state==='answering'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              самого быстропечатающего...</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state==='checking'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="'#ffcc00'" :artist="artist" :track="track" :turned="true"/>
        </v-row>
        <v-row align="center"
               justify="center" class="align-self-start">
          <div class="input-wrapper">

            <SmallFab @click="declineAnswer" type="check"/>
            <v-text-field
              disabled
              :height="100"
              solo
              :value="givenAnswer"
            />
            <SmallFab @click="acceptAnswer" type="cross"/>
          </div>
        </v-row>
      </template>

      <template v-if="state==='answered'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="artist" :track="track" :turned="answerIsCorrect!==undefined"/>
        </v-row>
      </template>

      <template v-if="state==='continuing'">
        <v-row align="center"
               justify="center" class="align-self-start">
          <BigFab @click="continueBtnHandler" text="Следующая песня"/>
        </v-row>
      </template>


    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import SmallFab from "@/components/SmallFab";
import FlipCard from "@/components/FlipCard";
import WS from "@/views/Game/Shared/ws";

export default {
  name: "Judge",
  components: {FlipCard, SmallFab, BigFab, NavPage},
  data: () => ({
    login: '',
    users: [],
    sessionId: '',

    judge: '',
    started: false,

    state: 'starting',
    states: ["starting", "ready", "answering", "checking", "answered", "continuing"],
    // starting, ready, answering, checking, answered, continuing

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
          this.judgeToStarting();
          break;
        case "ready":
          this.judgeToReady();
          break;
        case "answering":
          this.judgeToAnswering();
          break;
        case "checking":
          this.judgeToChecking();
          break;
        case "answered":
          this.judgeToAnswered();
          break;
        case "continuing":
          this.judgeToContinuing();
          break;
      }
    },

    //starting
    judgeToStarting() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState("starting");
    },
    async startBtnHandler() {
      let data_json = {"room_id": this.sessionId, "event_type": 1, "payload": {}};
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToReady();
    },

    //ready
    judgeToReady() {
      this.setAnswerIsCorrect(undefined);
      this.started = true;

      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState("ready");
    },

    //answering
    judgeToAnswering() {
      this.setState("answering");
    },

    //checking
    judgeToChecking() {
      this.setState("checking");
    },
    async declineAnswer() {
      const data_json = {
        "room_id": this.sessionId, "event_type": 2, "payload": {"answer_correct": false}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, false);
    },
    async acceptAnswer() {
      const data_json = {
        "room_id": this.sessionId, "event_type": 2, "payload": {"answer_correct": true}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, true);
    },

    //answered
    judgeToAnswered() {
      this.setState("answered");
    },

    //continuing
    judgeToContinuing() {
      this.setState("continuing");
    },
    async continueBtnHandler() {
      const data_json = {
        "room_id": this.sessionId, "event_type": 2, "payload": {"event": "next"}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToReady();
    }
  },
  mounted() {
    if (Object.keys(WS).length) {
      this.sessionId = WS.session;
      this.login = WS.login;
      this.judge = WS.judge;
    } else {
      this.$router.go(-1);
    }
  },
  beforeUpdate() {
    this.users = WS.users;
    this.started = WS.started;
  }
}
</script>

<style lang="scss" scoped>
.app {
  .v-input {
    font-size: 1.5em !important;
  }

  .v-label {
    font-size: 1.5em !important;
    padding: 0 20px;
  }

  .v-icon {
    font-size: 2.5em !important;
  }

  .v-btn {
    font-size: 1.5em !important;
  }

  .input-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 10px;
  }
}
</style>