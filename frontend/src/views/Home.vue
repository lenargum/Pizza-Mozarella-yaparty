<template>
  <NavPage :header="$options.name">
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";

export default {
  name: "Home",
  components: {NavPage}
}
</script>

<style scoped>

</style>