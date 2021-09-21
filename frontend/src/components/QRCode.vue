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
    <v-snackbar
      v-model="snackbar"
    >
      {{ error ? snackbarText.error : snackbarText.success }}

      <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="snackbar = false"
          :min-width="0"
        >
          <div class="qrcode__snackbar-icon">
            <svg viewBox="0 0 68 68" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M53.173 18.3379L49.2716 14.4365L33.8045 29.9036L18.3374 14.4365L14.436 18.3379L29.9031 33.805L14.436 49.2721L18.3374 53.1735L33.8045 37.7064L49.2716 53.1735L53.173 49.2721L37.7059 33.805L53.173 18.3379Z"
                fill="white"/>
            </svg>
          </div>
        </v-btn>
      </template>
    </v-snackbar>
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
  data: () => ({
    snackbar: false,
    error: false,
    snackbarText:
      {
        success: 'Ссылка для приглашения в вашу игру скопирована успешно! 🥳',
        error: 'Упс, скопировать не получилось ¯\\_(ツ)_/¯'
      }
  }),
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
        this.error = !document.execCommand('copy');
        this.snackbar = true;
      } catch (err) {
        this.error = true;
      }

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

  &__snackbar-icon {
    width: 3vw;
    height: 3vw;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>