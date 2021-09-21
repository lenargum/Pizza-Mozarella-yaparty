<template>
  <v-col cols="12" sm="11" md="11" lg="7" xl="5" :align-self="'center'" :align="'center'">
    <div class="qrcode__wrapper"
         @click.prevent="clickHandler"
         :style="{'--cursor': copyOnClick? 'pointer': 'initial'}"
         :title="copyOnClick? 'Скопировать ссылку в буфер': ''"
    >
      <VueQrcode
        :color="{ dark: '#222222', light: '#fff' }"
        :value="value"
        :width="240"
      />
    </div>
    <input class="qrcode__input-copy" type="hidden" id="testing-code" :value="value">
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
    },
    copyOnClick: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({}),
  methods: {
    clickHandler() {
      if (this.copyOnClick) {
        this.copyQRCodeLink();
      }
    },
    copyQRCodeLink() {
      let testingCodeToCopy = document.querySelector('#testing-code');
      testingCodeToCopy.setAttribute('type', 'text');
      testingCodeToCopy.select();

      try {
        let successful = document.execCommand('copy');
        if (successful) {
          alert('Ссылка для приглашения на вашу сессию скопирована успешно! 🥳');
        } else {
          alert('Упс, скопировать не получилось ¯\\_(ツ)_/¯');
        }
      } catch (err) {
        alert('Упс, скопировать не получилось ¯\\_(ツ)_/¯');
      }

      /* unselect the range */
      testingCodeToCopy.setAttribute('type', 'hidden');
      window.getSelection().removeAllRanges();
    },
  },
}
</script>

<style lang="scss" scoped>
.qrcode {
  &__wrapper {
    cursor: var(--cursor);
    width: min-content;
  }

  &__input-copy {
    //position: absolute;
    //top: -100px;
  }
}
</style>