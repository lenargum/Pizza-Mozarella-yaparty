<template>
  <NavPage :username="login" :users="users" :header="'Угадай мелодию'">
    <v-row align="center"
           justify="center" class="align-self-start">
      <v-spacer/>
      <BigFab @click="playerChoiceHandler" text="Стать игроком"/>
      <v-spacer/>
      <BigFab @click="judgeChoiceHandler" text="Стать ведущим"/>
      <v-spacer/>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";

export default {
  name: "ChooseRole",
  components: {BigFab, NavPage},
  data: () => ({
    login: 'username stub',
    users: [
      'stub1',
      'stub2'
    ],
    btnPressed: false,
    ws: null,
    sessionId: '12235'
  }),
  methods: {
    setUsers(users) {
      this.users = users;
    },
    setLogin(login) {
      this.login = login;
    },

    playerChoiceHandler() {
      // this.$router.push('/play/player');
    },
    async judgeChoiceHandler() {
      await this.connect();
      // this.$router.push('/play/judge');
    },


    connect() {
      // const path = window.location.hostname;
      const path = '84.201.167.68';
      const port = '4000';
      const login = 'lenar5';
      // const port = window.location.port;
      this.ws = new WebSocket("ws://" + path + ":" + port + "/ws/" + this.sessionId + "/connect?token=" + login);

      this.ws.onopen = () => {
        console.log('WebSocket opened');
        this.judge();
        // registering listeners
        this.ws.onmessage = (data) => console.log('Received data:', data.data);

        // sending data
        console.log('Sending data');
      }

      this.ws.onmessage = function (event) {
        console.log("ws:");
        console.log(event.data);
      };
    },
    judge() {
      const data_json = {"room_id": this.sessionId, "event_type": 2, "payload": {"update_role": true}};
      this.ws.send(JSON.stringify(data_json));
    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>