<template>
  <v-btn
    elevation="2"
    fab
    x-large
    :height="400"
    :width="400"
    @click="$emit('click')"
    :disabled="!active"
    :color="color"
  >
    <h2 class="text-h4">{{ text }}</h2>
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

<style scoped>

</style>