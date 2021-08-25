<template>
  <NavPage :username="login" :users="users" :header="'Угадай мелодию'">
    <v-row align="center"
           justify="center" class="align-self-start">
      <v-col cols="11" sm="10" md="10" lg="4" xl="4">
        <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Отсканируйте с вашего
          смартфона чтобы начать</h3>
        <v-row justify="center" align="center" no-gutters>
          <QRCode :value="qrcodeValue"/>
        </v-row>
      </v-col>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import QRCode from "@/components/QRCode";

export default {
  name: "CreateGame",
  components: {QRCode, NavPage},
  data: () => ({
    login: 'username stub',
    users: [
      'stub1',
      'stub2'
    ],
    btnPressed: false,
    qrcodeValue: "не ну а че)"
  }),
  methods: {
    setUsers(users) {
      this.users = users;
    },
    setLogin(login) {
      this.login = login;
    },
    setQrcode(value) {
      this.qrcodeValue = value;
    }
  }
}
</script>

<style lang="scss" scoped>
.app {

}
</style>