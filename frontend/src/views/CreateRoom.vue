<template>
  <NavPage>
    <template #default>
      <template v-if="!btnPressed">
        <v-row align="center"
               justify="center">
          <BigFab @click="btnPressed=true" text="Создать комнату"/>
        </v-row>
      </template>
      <template v-else>
        <HeaderTitle>Поделитесь с друзьями</HeaderTitle>
        <v-row align="center"
               justify="center" class="align-self-start">
          <v-col cols="11" sm="10" md="10" lg="4" xl="4">
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
    qrcodeValue: "не ну а че)"
  }),
  methods: {
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