<template>
  <NavPage :header="currentState==='login'? 'Логин': currentState==='role'? 'Угадай мелодию': 'unexpected state'"
           :username="username"
           :users="users"
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
        <BigFab @click="judgeChoiceHandler" text="Стать ведущим"/>
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
          console.log('Received:', data.data);
          let status = data.data.response_status;
          let payload = data.data.payload;


          switch (status) {
            case 1:

              break;
            case 2:

              break;
            case 3:
              switch (payload.event) {
                case "connected":
                  WS.users.append(atob(payload.client));
                  this.set(this.users, WS.users);
                  break;
                case "disconnected":
                  WS.users.splice(WS.users.indexOf(atob(payload.client)), 1);
                  break;
              }
              break;
            case 4:

              switch (payload.event) {
                case "judge":
                  WS.judge = atob(payload.judge);
                  break;
                case "play":
                  this.playerToStarting();
                  WS.started = true
              }
              break;
          }
        }
        this.currentState = "role";
      }
    },

    // from ChooseRole
    playerChoiceHandler() {
      this.$router.push('/play/player');
    },
    async judgeChoiceHandler() {
      const data_json = {"room_id": this.sessionId, "event_type": 2, "payload": {"update_role": true}};
      await WS.socket.send(JSON.stringify(data_json));
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