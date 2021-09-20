<template>
  <NavPage :header="currentState==='login'? 'Логин': currentState==='role'? 'Угадай мелодию': 'unexpected state'"
           :username="username"
           :users="users"
           :judge="judge"
  >
    <template v-if="currentState==='login'">
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
            :error="error"
            :error-messages="error?'Логин не должен быть пустым':''"
          />
        </template>
        <template #button>
          <SmallFab @click="loginHandler" type="forward"/>
        </template>
      </TextField>
    </template>
    <template v-else-if="currentState==='role'">
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

import WS from "@/views/Game/Shared/ws.js"
import server from "@/data/hosts";

export default {
  name: "MobileLogin",
  components: {
    TextField,
    SmallFab,
    NavPage,
    BigFab
  },
  data: () => ({
    states: ["login", "role"],
    currentState: "login",
    username: "",
    sessionId: "",
    error: false,
    users: [],

    // from ChooseRole
    login: '',
    judge: WS.judge
  }),
  methods: {
    loginHandler() {
      if (!this.username.length) {
        this.error = true;
        return;
      } else {
        this.error = false;
      }

      WS.login = this.username;
      WS.session = this.sessionId;
      WS.socket = new WebSocket("ws://" + server.hostname + ":" + server.port + "/ws/" + this.sessionId + "/connect?token=" + this.username);

      WS.socket.onopen = () => {
        console.log('WebSocket opened');

        WS.socket.onmessage = (data) => {
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
        }
        this.currentState = "role";
      }
    },
    setJudge(user) {
      if (user) {
        console.log("USER '" + user + "' IS JUDGE");
      } else {
        console.log("NO JUDGE");
      }

      this.judge = user;
      WS.judge = user;
    },
    setUsers(users) {
      this.users = users;
      WS.users = users;
    },
    userConnected(user) {
      console.log("USER CONNECTED: " + "'" + user + "'");
      let temp_users = this.users;
      temp_users.push(user);

      WS.users = temp_users;
      this.users = temp_users;
    },
    userDisconnected(user) {
      console.log("USER DISCONNECTED: " + "'" + user + "'");
      let temp_users = this.users;
      temp_users.splice(temp_users.indexOf(user), 1);

      WS.users = temp_users;
      this.users = temp_users;

      if (this.judge === user) {
        this.setJudge('');
      }
    },

    // from ChooseRole
    playerChoiceHandler() {
      this.$router.push('/play/player');
    },
    async judgeChoiceHandler() {
      const judge_role_request_json = {"session_id": this.sessionId, "event_type": 2, "payload": {"update_role": true}};
      await WS.socket.send(JSON.stringify(judge_role_request_json));
      await this.$router.push('/play/judge');
    },
  },
  mounted() {
    if (this.$route.params.sessionId) {
      this.sessionId = this.$route.params.sessionId;
    } else {
      this.$router.go(-1);
    }
  }
}
</script>