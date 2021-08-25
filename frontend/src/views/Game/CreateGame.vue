<template>
  <NavPage :header="'Угадай мелодию'">
    <SmallFab v-if="!loading" class="next-btn" @click="nextPageBtnHandler" type="forward"/>
    <v-row align="center"
           justify="center" class="align-self-start">
      <template v-if="loading">
        <v-progress-circular
          :size="70"
          :width="7"
          color="#ffcc00"
          indeterminate
        ></v-progress-circular>
      </template>
      <template v-else>
        <v-col cols="11" sm="10" md="10" lg="7" xl="7">
          <h3 class="text-h5 text-sm-h4 text-md-h3 text-lg-h3 text-xl-h2" style="text-align: center">Отсканируйте с
            вашего
            смартфона чтобы начать</h3>
          <v-row justify="center" align="center" no-gutters>
            <QRCode :value="qrcodeValue"/>
          </v-row>
        </v-col>
      </template>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import QRCode from "@/components/QRCode";
import SmallFab from "@/components/SmallFab";

export default {
  name: "CreateGame",
  components: {SmallFab, QRCode, NavPage},
  data: () => ({
    btnPressed: false,
    qrcodeValue: "не ну а че)",
    localPath: '',
    loading: true,
  }),
  methods: {
    nextPageBtnHandler() {
      this.$router.push(this.localPath);
    }
  },
  async created() {
    const requestOptions = {
      method: "POST",
      headers: {"Content-Type": "application/json"},
    };
    const response = await fetch("https://secure-ridge-64426.herokuapp.com/http://84.201.167.68:4000/session/create", requestOptions);
    console.log(response);
    const data = await response.json();
    console.log(data);
    console.log(data.session_id);
    this.localPath = "/mobileLogin/" + data.session_id;
    this.qrcodeValue = window.location.protocol + "//" + window.location.host + this.localPath;
    this.loading = false;
  }
}
</script>

<style lang="scss" scoped>
.app {
  .next-btn {
    position: absolute;
    transform: translate(-50%, -50%);
    top: 50vh;
    right: 0;
  }
}
</style>