<template>
  <NavPage>
    <template>
      <CurrentUsers :users="users"/>
      <v-row align="start" justify="center" class="align-self-start" no-gutters>
        <HeaderTitle>Угадай мелодию</HeaderTitle>
      </v-row>
      <v-row align="center"
             justify="center" class="align-self-start">
        <v-col cols="11" sm="10" md="10" lg="4" xl="4">
          <h3 class="text-h3" style="text-align: center">Отсканируйте с вашего смартфона чтобы начать</h3>
          <v-row justify="center" no-gutters>
            <QRCode value="не ну а че)"/>
          </v-row>
        </v-col>
      </v-row>
    </template>
    <template #username>
      <div class="text-h4">{{ login }}</div>
    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import QRCode from "@/components/QRCode";
import HeaderTitle from "@/components/HeaderTitle";
import CurrentUsers from "@/components/CurrentUsers";

export default {
  name: "CreateGame",
  components: {CurrentUsers, HeaderTitle, QRCode, NavPage},
  data: () => ({
    login: 'petya',
    users: [
      'aaaaaa',
      'bbbbbbbb'
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
  }
}
</script>

<style lang="scss" scoped>
.app {

}
</style>