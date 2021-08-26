<template>
  <NavPage :header="'Логин'" :username="username">
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
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";

import WS from "@/views/Game/Shared/ws.js"

export default {
  name: "MobileLogin",
  components: {TextField, SmallFab, NavPage},
  data: () => ({
    username: "",
    sessionId: "",
    error: false
  }),
  methods: {
    loginHandler() {
      if (!this.username.length) {
        this.error = true;
        return;
      } else {
        this.error = false;
      }

      const path = '84.201.167.68';
      const port = '4000';

      WS.login = this.username;
      WS.session = this.sessionId;
      WS.socket = new WebSocket("ws://" + path + ":" + port + "/ws/" + this.sessionId + "/connect?token=" + this.username);

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
                  this.setState("starting");
                  WS.started = true
              }
              break;
          }
        }
        this.$router.push('/play');
      }
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