<template>
  <NavPage
    :username="login"
    :users="users"
    :score="score.toString()"
    :header="'Угадай мелодию'"
  >
    <template #debug>
      <v-btn v-for="state in states"
             @click="setState(state)"
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
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Ждем
              остальных...</h3>
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

      </template>

      <template v-if="state==='waiting'">

      </template>

      <template v-if="state==='waited'">

      </template>


    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";

export default {
  name: "Player",
  components: {TextField, SmallFab, BigFab, NavPage},
  data: () => ({
    login: 'username stub',
    users: [
      'stub1',
      'stub2'
    ],
    score: 100,
    state: 'starting',
    states: ["starting", "ready", "answering", "answered", "waiting", "waited"],
    // starting, ready, answering, answered, waiting, waited

    givenAnswer: '',
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

    //starting

    //ready
    answerBtnHandler() {
      // check if he was fast enough, instead of true
      const answering = true;

      if (answering) {
        this.setState("answering");
      } else {
        this.setState("waiting");
      }
    },

    //answering
    submitAnswerBtnHandler() {
      const answerCorrect = true;

      if (answerCorrect) {
        this.setState("answered");
      }
      this.givenAnswer = "";
    }

    //answered


    //waiting

    //waited

  }
}
</script>

<style scoped>

</style>