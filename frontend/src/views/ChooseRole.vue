<template>
  <NavPage :username="login" :users="users" :header="'Угадай мелодию'">
    <v-row align="center"
           justify="center" class="align-self-start">
      <v-spacer/>
      <BigFab @click="$router.push('/player')" text="Стать игроком"/>
      <v-spacer/>
      <BigFab @click="$router.push('/judge')" text="Стать ведущим"/>
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
  }),
  methods: {
    setUsers(users) {
      this.users = users;
    },
    setLogin(login) {
      this.login = login;
    }
  },
  mounted() {

  }
}
</script>

<style scoped>

</style>