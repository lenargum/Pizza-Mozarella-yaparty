<template>
  <v-btn
    :class="'small-fab'"
    elevation="2"
    fab
    x-large
    :height="'7vw'"
    :width="'7vw'"
    @click="$emit('click')"
    :color="type==='back'? '#6DAAE8' : type==='forward'? '#FFCC00' : type==='check'? '#4CAF50' : type==='cross'? '#FC3F1D': type==='home'? '#FFCC00': undefined"
  >
    <template v-if="type==='back'">
      <div class="icon-wrapper" style="margin-left: -12px">
        <svg width="71" height="71" viewBox="0 0 71 71" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M53.7236 58.8774L30.6502 35.8039L53.7236 12.7304L47.516 6.52283L18.235 35.8039L47.516 65.085L53.7236 58.8774Z"
            fill="white"/>
        </svg>
      </div>
    </template>

    <template v-if="type==='forward'">
      <div class="icon-wrapper" style="margin-right: -12px">
        <svg width="71" height="71" viewBox="0 0 71 71" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M17.2754 12.1226L40.3489 35.1961L17.2754 58.2696L23.483 64.4772L52.764 35.1961L23.483 5.91504L17.2754 12.1226Z"
            fill="black"/>
        </svg>
      </div>
    </template>

    <template v-if="type==='check'">
      <div class="icon-wrapper">
        <svg width="68" height="68" viewBox="0 0 68 68" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M25.5032 45.7262L13.9652 34.1881L10.0361 38.0895L25.5032 53.5566L58.7063 20.3535L54.805 16.4521L25.5032 45.7262Z"
            fill="white"/>
        </svg>
      </div>
    </template>

    <template v-if="type==='cross'">
      <div class="icon-wrapper">
        <svg width="68" height="68" viewBox="0 0 68 68" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M53.173 18.3379L49.2716 14.4365L33.8045 29.9036L18.3374 14.4365L14.436 18.3379L29.9031 33.805L14.436 49.2721L18.3374 53.1735L33.8045 37.7064L49.2716 53.1735L53.173 49.2721L37.7059 33.805L53.173 18.3379Z"
            fill="white"/>
        </svg>
      </div>
    </template>

    <template v-if="type==='text'">
      <div class="text-h8">{{ text }}</div>
    </template>

    <template v-if="type==='home'">
      <div class="icon-wrapper">
        <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 40V28H28V40H38V24H44L24 6L4 24H10V40H20Z" fill="black"/>
        </svg>
      </div>
    </template>
  </v-btn>
</template>

<script>
export default {
  name: "SmallFab",
  props: {
    type: {
      // back, forward, check, cross, text
      type: String,
      required: true
    },
    text: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.icon-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 5vw;
  height: 5vw;
  min-height: 50px;
  min-width: 50px;
}

.small-fab {
  position: relative;
  min-height: 80px;
  min-width: 80px;
}
</style>


