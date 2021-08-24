<template>
  <VueQrcode :value="value" :width="240"/>
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

<style scoped>

</style>