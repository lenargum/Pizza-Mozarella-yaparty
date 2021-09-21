<template>
  <NavPage
    :username="username"
    :users="users"
    :header="'Угадай мелодию'"
    :judge="judge"
  >
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
          <v-col cols="11" sm="10" md="10" lg="9" xl="8" align="center">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем самого
              быстрого 🚀</h3>
            <v-spacer :style="{height: '5vw'}"/>
            <WaitingLoader/>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Judge.ANSWERING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="9" xl="8" align="center">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">
              {{ answeringPlayer + " отвечает" }}</h3>
            <v-spacer :style="{height: '5vw'}"/>
            <WaitingLoader/>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Judge.CHECKING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="'#ffcc00'" :artist="song.author" :track="song.name" :turned="true"/>
        </v-row>
        <v-row align="center"
               justify="center" class="align-self-start">
          <div class="input-wrapper">

            <SmallFab @click="acceptAnswer" type="check"/>
            <v-text-field
              disabled
              :height="100"
              solo
              :value="givenAnswer"
            />
            <SmallFab @click="declineAnswer" type="cross"/>
          </div>
        </v-row>
      </template>

      <template v-if="state===states.Judge.ANSWERED">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="song.author" :track="song.name" :turned="answered"/>
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
import WaitingLoader from "@/components/WaitingLoader";
import States from "@/views/Games/Game/Shared/States";

export default {
  name: "Judge",
  components: {WaitingLoader, FlipCard, SmallFab, BigFab, NavPage},
  props: {
    username: String,
    users: Array,
    sessionId: String,
    judge: String,
    state: String,
    WS: WebSocket,
    answeringPlayer: String,
    givenAnswer: String,
    song: Object,
    answerIsCorrect: Boolean,
  },
  data: () => ({
    states: States,
    answered: false,
  }),
  methods: {
    setAnswered(value) {
      this.answered = value;
    },
    async startBtnHandler() {
      let data_json = {"session_id": this.sessionId, "event_type": 1, "payload": {}};
      await this.WS.send(JSON.stringify(data_json));
    },
    async declineAnswer() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer": this.givenAnswer, "answer_correct": false}
      };
      await this.WS.send(JSON.stringify(data_json));
      this.$emit("changeState", States.Judge.ANSWERED);
      setTimeout(this.setAnswered, 3000, true);
      setTimeout(() => (this.$emit("changeState", States.Judge.CONTINUE)), 5000);
    },
    async acceptAnswer() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer": this.givenAnswer, "answer_correct": true}
      };
      await this.WS.send(JSON.stringify(data_json));
      this.$emit("changeState", States.Judge.ANSWERED);
      setTimeout(this.setAnswered, 3000, true);
      setTimeout(() => (this.$emit("changeState", States.Judge.CONTINUE)), 5000);
    },
    async continueBtnHandler() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"event": "next"}
      };
      await this.WS.send(JSON.stringify(data_json));
      this.setAnswered(false);
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