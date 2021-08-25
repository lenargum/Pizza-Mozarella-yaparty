<template>
  <NavPage>
    <template #default>
      <template v-if="!btnPressed">
        <v-row align="center"
               justify="center">
          <BigFab @click="btnHandler" text="Создать комнату"/>
        </v-row>
      </template>
      <template v-else>
        <HeaderTitle>Поделитесь с друзьями</HeaderTitle>
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="7" xl="7">
            <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Позвольте друзьям
              отсканировать QR-код чтобы присоединиться к
              комнате</h3>
            <v-row justify="center" no-gutters>
              <QRCode :value="qrcodeValue"/>
            </v-row>
          </v-col>
        </v-row>
      </template>
    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import QRCode from "@/components/QRCode";
import HeaderTitle from "@/components/HeaderTitle";

export default {
  name: "CreateRoom",
  components: {HeaderTitle, QRCode, BigFab, NavPage},
  data: () => ({
    btnPressed: false,
    qrcodeValue: undefined,
    link: "",
  }),
  methods: {
    setQrcode(value) {
      this.qrcodeValue = value;
    },
    async btnHandler() {
      const requestOptions = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
      };
      const response = await fetch("https://secure-ridge-64426.herokuapp.com/http://84.201.167.68:8000/room/create", requestOptions);
      const data = await response.json();
      this.qrcodeValue = data.session_id;
      this.btnPressed = true;

      this.link = "http://84.201.167.68:5000/login?room_id=" + this.qrcodeValue;
    }
  }
}
</script>

<style lang="scss" scoped>
.app {

}
</style>