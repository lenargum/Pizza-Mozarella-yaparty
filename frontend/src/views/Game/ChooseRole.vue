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

import WS from "@/views/Game/Shared/ws.js"

export default {
  name: "ChooseRole",
  components: {BigFab, NavPage},
  props: {
    users: Array,
  },
  data: () => ({
    login: '',
    sessionId: WS.started,
    judge: WS.judge
  }),
  methods: {
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
    if (Object.keys(WS).length) {
      this.sessionId = WS.session;
      this.login = WS.login;
    } else {
      this.$router.go(-1);
    }
  },
}
</script>

<style scoped>

</style>