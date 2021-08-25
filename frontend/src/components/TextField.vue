<template>
  <v-row
    justify="center" class="align-self-start">
    <v-col cols="11" sm="6" md="6" lg="4" xl="2" align-self="center">
      <slot/>
    </v-col>
    <v-col cols="3" sm="2" md="1" lg="1" xl="1" align-self="start">
      <slot name="button"/>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.app {
  .v-input {
    font-size: 1.5em !important;
  }

  .v-label {
    font-size: 1.5em !important;
    padding: 0 20px;
  }

  .v-icon {
    font-size: 2.5em !important;
  }
}
</style>