<template>
  <v-btn
    elevation="2"
    fab
    x-large
    :height="100"
    :width="100"
    @click="$emit('click')"
    :color="type==='back'? '#6DAAE8' : type==='forward'? '#FFCC00' : undefined"
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

    <template v-if="type==='text'">
      <div class="text-h8">{{ text }}</div>
    </template>
  </v-btn>
</template>

<script>
export default {
  name: "SmallFab",
  props: {
    type: {
      // back, forward, text
      type: String,
      default: ''
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
}
</style>


