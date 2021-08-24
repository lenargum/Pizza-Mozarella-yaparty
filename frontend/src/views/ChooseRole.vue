<template>
  <NavPage>
    <template #default>
      <CurrentUsers :users="users"/>
      <v-row align="start" justify="center" class="align-self-start" no-gutters>
        <HeaderTitle>Угадай мелодию</HeaderTitle>
      </v-row>
      <v-row align="center"
             justify="center" class="align-self-start">
        <v-spacer/>
        <BigFab @click="$router.push('/play/player')" text="Стать игроком"/>
        <v-spacer/>
        <BigFab @click="$router.push('/play/judge')" text="Стать ведущим"/>
        <v-spacer/>
      </v-row>
    </template>
    <template #username>
      <div class="text-h4">{{ login }}</div>
    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import HeaderTitle from "@/components/HeaderTitle";
import CurrentUsers from "@/components/CurrentUsers";
import BigFab from "@/components/BigFab";

export default {
  name: "ChooseRole",
  components: {BigFab, CurrentUsers, HeaderTitle, NavPage},
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