<template>
  <NavPage
    :username="username"
    :users="users"
    :header="'Угадай мелодию'"
    :judge="judge"
  >
    <template v-if="judge===username" #debug>
      Judge debugger
      <v-btn v-for="state in states.Judge"
             @click="stateSwitcher(state)"
             :key="state"
             :disabled="state===$data.state"
      >{{ state }}
      </v-btn>
    </template>
    <template>

      <template v-if="state===states.Judge.STARTING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <BigFab @click="startBtnHandler" text="Начать игру"/>
        </v-row>
      </template>

      <template v-if="state===states.Judge.READY">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              самого быстрого...</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Judge.ANSWERING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              самого быстропечатающего...</h3>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Judge.CHECKING">
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

      <template v-if="state===states.Judge.ANSWERED">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="artist" :track="track" :turned="answerIsCorrect!==undefined"/>
        </v-row>
      </template>

      <template v-if="state===states.Judge.CONTINUE">
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
import WS from "@/views/Games/Game/Shared/ws";
import States from "@/views/Games/Game/Shared/States";

export default {
  name: "Judge",
  components: {FlipCard, SmallFab, BigFab, NavPage},
  data: () => ({
    username: '',
    users: [],
    sessionId: '',

    judge: '',
    started: false,

    states: States,
    state: this.states.Judge.STARTING,


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
        case this.states.Judge.STARTING:
          this.judgeToStarting();
          break;
        case this.states.Judge.READY:
          this.judgeToReady();
          break;
        case this.states.Judge.ANSWERING:
          this.judgeToAnswering();
          break;
        case this.states.Judge.CHECKING:
          this.judgeToChecking();
          break;
        case this.states.Judge.ANSWERED:
          this.judgeToAnswered();
          break;
        case this.states.Judge.CONTINUE:
          this.judgeToContinue();
          break;
      }
    },

    //j_starting
    judgeToStarting() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState(States.Judge.STARTING);
    },
    async startBtnHandler() {
      let data_json = {"session_id": this.sessionId, "event_type": 1, "payload": {}};
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToReady();
    },

    //j_ready
    judgeToReady() {
      this.setAnswerIsCorrect(undefined);
      this.started = true;

      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState(States.Judge.READY);
    },

    //j_answering
    judgeToAnswering() {
      this.setState(States.Judge.ANSWERING);
    },

    //j_checking
    judgeToChecking() {
      this.setState(States.Judge.CHECKING);
    },
    async declineAnswer() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer_correct": false}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, false);
    },
    async acceptAnswer() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer_correct": true}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, true);
    },

    //j_answered
    judgeToAnswered() {
      this.setState(States.Judge.ANSWERED);
    },

    //j_continue
    judgeToContinue() {
      this.setState(States.Judge.CONTINUE);
    },
    async continueBtnHandler() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"event": "next"}
      };
      await WS.socket.send(JSON.stringify(data_json));

      this.judgeToReady();
    }
  },
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