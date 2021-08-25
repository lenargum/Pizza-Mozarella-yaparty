<template>
  <v-col cols="12" sm="11" md="11" lg="7" xl="5" :align-self="'center'" :align="'center'">
    <VueQrcode class="qrcode__wrapper" :color="{ dark: '#222222', light: '#fff' }" :value="value" :width="240"/>
  </v-col>

</template>

<script>
import VueQrcode from 'vue-qrcode'

export default {
  name: "QRCode",
  components: {
    VueQrcode
  },
  props: {
    value: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
</style>