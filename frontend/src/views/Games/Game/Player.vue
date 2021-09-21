<template>
  <NavPage
    :header="'Угадай мелодию'"
    :username="username"
    :users="users"
    :score="score"
    :judge="judge"
  >
    <template>
      <template v-if="state===states.Player.STARTING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="9" xl="8">
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
              placeholder="Ответ"
              v-model="answer"
              @keydown.enter="submitAnswerBtnHandler"
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
                    :artist="song.author" :track="song.name" :turned="answerIsCorrect!==undefined"/>
        </v-row>
        <v-row align="center"
               justify="center" class="align-self-start">
          <div class="answer-wrapper">
            <v-text-field
              disabled
              :height="100"
              solo
              :value="givenAnswer"
            />
          </div>
        </v-row>
      </template>

      <template v-if="state===states.Player.WAITING">
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="9" xl="8" align="center">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">
              {{
                answeringPlayer === username ? "Оценка ответа от независимых экспертов 🧐" : (answeringPlayer + " отвечает")
              }}
            </h3>
            <v-spacer :style="{height: '5vw'}"/>
            <WaitingLoader/>
          </v-col>
        </v-row>
      </template>

      <template v-if="state===states.Player.WAITED">
        <v-row align="center"
               justify="center" class="align-self-start">
          <FlipCard :answer-color="answerIsCorrect===undefined? '#ffcc00': answerIsCorrect? '#5acc5eff': '#FC3F1D'"
                    :artist="song.author" :track="song.name" :turned="answerIsCorrect!==undefined"/>
        </v-row>

        <v-row align="center"
               justify="center" class="align-self-start">
          <div class="answer-wrapper answer-wrapper_waited">
            <h4 class="text-h7 text-sm-h6 text-md-h5 text-lg-h5 text-xl-h4" style="text-align: start; padding-left: 8%">
              {{ answeringPlayer + ":" }}
            </h4>
            <v-text-field
              disabled
              :height="100"
              solo
              :value="givenAnswer"
            />
          </div>
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
import States from "@/views/Games/Game/Shared/States";
import WaitingLoader from "@/components/WaitingLoader";

export default {
  name: "Player",
  components: {WaitingLoader, FlipCard, TextField, SmallFab, BigFab, NavPage},
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
    score: String,
  },
  data: () => ({
    states: States,
    // p_starting, p_ready, p_answering, p_answered, p_waiting, p_waited

    answer: '',
  }),
  methods: {
    async answerBtnHandler() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"event": "answer"}
      };
      await this.WS.send(JSON.stringify(data_json));
    },

    async submitAnswerBtnHandler() {
      const data_json = {
        "session_id": this.sessionId, "event_type": 2, "payload": {"answer": this.answer}
      };
      await this.WS.send(JSON.stringify(data_json));
      this.answer = "";
      this.$emit("changeState", States.Player.WAITING);
    },
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

  .answer-wrapper {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;

    &_waited {
      margin-top: -5vw;
    }
  }
}
</style>