<template>
  <v-btn
    class="big-fab"
    elevation="2"
    fab
    x-large
    :height="'20vw'"
    :width="'20vw'"
    @click="$emit('click')"
    :disabled="!active"
    :color="color"
  >
    <span class="big-fab__span text-h6 text-sm-h6 text-md-h5 text-lg-h5 text-xl-h4">{{ text }}</span>
  </v-btn>
</template>

<script>
export default {
  name: "BigFab",
  props: {
    text: {
      type: String,
      default: ''
    },
    active: {
      type: Boolean,
      default: true
    },
    color: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.app {
  .big-fab {
    min-width: 180px;
    min-height: 180px;

    &__span {
      width: 75%;
      word-break: normal;
      white-space: break-spaces;
    }
  }
}
</style>