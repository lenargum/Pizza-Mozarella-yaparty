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
            <SmallFab @click="declineAnswer" type="text" text="-"/>
            <v-text-field
              disabled
              :height="100"
              solo
              :value="givenAnswer"
            />
            <SmallFab @click="acceptAnswer" type="text" text="+"/>
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

export default {
  name: "Judge",
  components: {FlipCard, SmallFab, BigFab, NavPage},
  data: () => ({
    login: 'username stub',
    users: [
      'stub1',
      'stub2'
    ],
    state: 'starting',
    states: ["starting", "ready", "answering", "checking", "answered", "continuing"],
    // starting, ready, answering, checking, answered, continuing

    answerIsCorrect: undefined,
    givenAnswer: 'пошлая молли',
    track: 'Новый мерин',
    artist: 'Моргенштерн',
  }),
  methods: {
    setUsers(users) {
      this.users = users;
    },
    setLogin(login) {
      this.login = login;
    },
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
        case "checking":
          this.toChecking();
          break;
        case "answered":
          this.toAnswered();
          break;
        case "continuing":
          this.toContinuing();
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
    startBtnHandler() {
      this.toReady();
    },

    //ready
    toReady() {
      this.setAnswerIsCorrect(undefined);
      this.givenAnswer = '';
      this.track = '';
      this.artist = '';
      this.setState("ready");
    },

    //answering
    toAnswering() {
      this.setState("answering");
    },

    //checking
    toChecking() {
      this.setState("checking");
    },
    declineAnswer() {
      // todo: send decline
      this.toAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, false);
    },
    acceptAnswer() {
      // todo: send accept
      this.toAnswered();
      setTimeout(this.setAnswerIsCorrect, 3000, true);
    },


    //answered
    toAnswered() {
      this.setState("answered");
    },

    //continuing
    toContinuing() {
      this.setState("continuing");
    },
    continueBtnHandler() {
      // todo: start next round completely
      this.toReady();
    }

  }
}
</script>

<style lang="scss" scoped>
.app {
  .v-input {
    font-size: 1.5rem !important;
  }

  .v-label {
    font-size: 1.5rem !important;
    padding: 0 20px;
  }

  .v-icon {
    font-size: 2.5rem !important;
  }

  .v-btn {
    font-size: 1.5rem !important;
  }

  .input-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    gap: 10px;
  }
}
</style>