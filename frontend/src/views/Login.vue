<template>
  <NavPage>
    <h1 style="text-align: center">{{ $options.name }}</h1>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";

export default {
  name: "Login",
  components: {NavPage}
}
</script>

<style scoped>

</style>