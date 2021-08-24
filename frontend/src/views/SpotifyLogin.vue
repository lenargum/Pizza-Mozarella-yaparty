<template>
  <NavPage>
    <template v-if="btnPressed===false">
      <v-row align="start" justify="center" class="align-self-start" no-gutters>
        <HeaderTitle>Подключение аккаунта Spotify</HeaderTitle>
      </v-row>
      <v-row align="center"
             justify="center" class="align-self-start">
        <BigFab @click="_handleSpotifyConnect(); btnPressed=true" text="Войти"/>
      </v-row>
    </template>
    <template v-else-if="btnPressed===true && login===false">
      <v-row align="start" justify="center" class="align-self-start" no-gutters>
        <HeaderTitle>Вечеринка только для подключивших Spotify...</HeaderTitle>
      </v-row>
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
            <SmallFab @click="$router.push('/login')" type="text" text="HACKS"/>
          </v-row>
        </v-col>
      </v-row>
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
    login: false,
    btnPressed: false
  }),
  methods: {
    _handleSpotifyConnect() {
      if (this.btnPressed === true && this.login === false) {
        // try connect
        // this.login = true;
      }
    },
  }
}
</script>

<style scoped>

</style>