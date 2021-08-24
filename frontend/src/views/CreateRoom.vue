<template>
  <NavPage>
    <template v-if="!btnPressed">
      <v-row align="center"
             justify="center">
        <BigFab @click="btnPressed=true" text="Создать комнату"/>
      </v-row>
    </template>
    <template v-else>
      <v-row align="start" justify="center" class="align-self-start" no-gutters>
        <Title>Поделитесь с друзьями</Title>
      </v-row>
      <v-row align="center"
             justify="center" class="align-self-start">
        <v-col cols="6">
          <h3 class="text-h3" style="text-align: center">Позвольте друзьям отсканировать QR-код чтобы присоединиться к
            комнате</h3>
          <v-row justify="center" no-gutters>
            <QRCode value="не ну а че)"/>
          </v-row>
        </v-col>
      </v-row>
    </template>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import BigFab from "@/components/BigFab";
import QRCode from "@/components/QRCode";
import Title from "@/components/Title";

export default {
  name: "CreateRoom",
  components: {Title, QRCode, BigFab, NavPage},
  data: () => ({
    btnPressed: false,
  }),
}
</script>

<style lang="scss" scoped>
.app {

}
</style>