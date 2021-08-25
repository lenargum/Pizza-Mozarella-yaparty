<template>
  <NavPage>
    <template #default>
      <template v-if="btnPressed===false">
        <HeaderTitle>Подключение аккаунта Spotify</HeaderTitle>
        <v-row align="center"
               justify="center" class="align-self-start">
          <BigFab @click="_handleSpotifyConnect(); btnPressed=true" text="Войти"/>
        </v-row>
      </template>
      <template v-else-if="btnPressed===true && loginIsOk===false">
        <HeaderTitle>Вечеринка только для подключивших Spotify...</HeaderTitle>
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="6">
            <v-row justify="center" no-gutters>
              <v-img
                :src="require('../assets/closed.png')"
                :max-height="491"
                :max-width="491"
              />
            </v-row>
            <v-row justify="center">
              <SmallFab @click="btnPressed=false" type="back"/>
            </v-row>
          </v-col>
        </v-row>
      </template>
    </template>
    <template #debug>
      <v-btn @click="loginIsOk=true" v-text="'Imitate Spotify login'"/>
    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import HeaderTitle from "@/components/HeaderTitle";
import SmallFab from "@/components/SmallFab";

export default {
  name: "SpotifyLogin",
  components: {SmallFab, HeaderTitle, BigFab, NavPage},
  data: () => ({
    loginIsOk: false,
    btnPressed: false,
    roomId: ''
  }),
  methods: {
    _handleSpotifyConnect() {
      if (this.btnPressed === true && this.loginIsOk === false) {


        // this.login = true;
        this.$router.push('/home/' + this.roomId);
      }
    },
  },
  mounted() {
    this.roomId = this.$route.params.id;
  }
}
</script>

<style scoped>

</style>