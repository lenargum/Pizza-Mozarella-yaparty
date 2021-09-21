<template>
  <v-row
    justify="center" align="center" class="align-self-start">
    <v-col cols="11" sm="6" md="6" lg="5" xl="2" align-self="center">
      <slot/>
    </v-col>
    <v-col cols="3" sm="2" md="1" lg="1" xl="1" align-self="center" :style="{marginBottom: '30px'}">
      <slot name="button"/>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.app {
  .v-input {
    font-size: 1.5em !important;

    &__icon--clear {
      .v-icon {
        color: $style_grey !important;
        font-size: 2em !important;

        &:hover {
          color: $style_black !important;
        }
      }
    }
  }

  .v-label {
    font-size: 1.5em !important;
    padding: 0 20px;
  }
}
</style>