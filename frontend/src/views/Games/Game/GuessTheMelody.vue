<template>
  <NavPage :header="currentState===states.LOGIN? 'Логин': 'Угадай мелодию'"
           :username="username"
           :users="users"
           :judge="judge"
  >
    <template v-if="currentState===states.CREATE">
      <SmallFab v-if="!loading" class="next-btn" @click="createGameBtnHandler" type="forward"/>
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
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Отсканируйте с
              вашего
              смартфона чтобы начать</h3>
            <v-row justify="center" align="center" no-gutters>
              <QRCode :value="qrcodeValue"/>
            </v-row>
          </v-col>
        </template>
      </v-row>
    </template>
    <template v-else-if="currentState===states.LOGIN">
      <TextField>
        <template #default>
          <v-text-field
            autofocus
            clearable
            :counter="10"
            :height="100"
            solo
            v-model="username"
            :maxlength="10"
            :error="loginError"
            :error-messages="loginError?'Логин не должен быть пустым':''"
          />
        </template>
        <template #button>
          <SmallFab @click="loginHandler" type="forward"/>
        </template>
      </TextField>
    </template>
    <template v-else-if="currentState===states.ROLE">
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

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";
import BigFab from "@/components/BigFab";
import QRCode from "@/components/QRCode";

import server from "@/data/hosts";

export default {
  name: "MobileLogin",
  components: {
    TextField,
    SmallFab,
    NavPage,
    BigFab,
    QRCode,
  },
  data: () => ({
    states: {
      CREATE: "create",
      LOGIN: "login",
      ROLE: "role"
    },
    currentState: "create",
    sessionId: "",
    username: "",
    users: [],
    judge: '',
    WS: undefined,

    // create
    btnPressed: false,
    qrcodeValue: "не ну а че)",
    sessionURL: '',
    loading: true,

    // login
    loginError: false,


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

    // HANDLERS

    // HANDLERS - CREATE
    createGameBtnHandler() {
      this.$router.push(this.sessionURL);
    },

    // HANDLERS - LOGIN
    loginHandler() {
      if (!this.username.length) {
        this.loginError = true;
        return;
      } else {
        this.loginError = false;
      }

      this.WS = new WebSocket("ws://" + server.hostname + ":" + server.port + "/ws/" + this.sessionId + "/connect?token=" + this.username);

      this.WS.onopen = () => {
        console.log('WebSocket opened');

        this.WS.onmessage = (data) => {
          this.serverMessagesHandler(data);
        }
        this.currentState = this.states.ROLE;
      }
    },

    // HANDLERS - ROLE
    playerChoiceHandler() {
      this.$router.push('/play/player');
    },
    async judgeChoiceHandler() {
      const judge_role_request_json = {"session_id": this.sessionId, "event_type": 2, "payload": {"update_role": true}};
      await this.WS.send(JSON.stringify(judge_role_request_json));
      await this.$router.push('/play/judge');
    },

    // HANDLERS - COMMON
    async sessionIdHandler(sessionId) {
      if (sessionId) {
        this.currentState = this.states.LOGIN;
        this.sessionId = sessionId;
      } else {
        this.currentState = this.states.CREATE;
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
        this.loading = false;
      }
    },
    serverMessagesHandler(data) {
      let response;
      try {
        response = JSON.parse(data.data);
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
          if (payload.clients) {
            this.setUsers(payload.clients.map((client_base64) => (atob(client_base64))));
            if (payload.judge) this.setJudge(atob(payload.judge));
          }
          break;
        case 2:

          break;
        case 3:
          switch (payload.event) {
            case "connected":
              this.userConnected(atob(payload.client));
              break;
            case "disconnected":
              this.userDisconnected(atob(payload.client));
              break;
          }
          break;
        case 4:

          switch (payload.event) {
            case "judge":
              this.setJudge(atob(payload.judge));
              break;
            case "play":
            // TODO: handle start of the game

            // this.playerToStarting();
            // WS.started = true
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
  .next-btn {
    position: absolute;
    transform: translate(-50%, -50%);
    top: 50vh;
    right: 0;
  }
}
</style>