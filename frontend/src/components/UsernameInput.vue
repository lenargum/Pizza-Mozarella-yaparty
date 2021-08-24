<template>
  <v-text-field
    @input="_handleInput"
    autofocus
    clearable
    :counter="max"
    :height="100"
    solo
    :value="value"
    :maxlength="max"
  />
</template>

<script>
export default {
  name: "UsernameInput",
  props: {
    value: String
  },
  data: () => ({
    max: 10,
  }),
  methods: {
    _handleInput(value) {
      this.$emit('input', value);
    }
  }
}
</script>

<style scoped>
.app .v-input {
  font-size: 1.5em;
}
</style>