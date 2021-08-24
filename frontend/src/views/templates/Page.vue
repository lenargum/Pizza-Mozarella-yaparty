<template>
  <v-app>
    <v-main>
      <slot name="default"/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Page",
}
</script>