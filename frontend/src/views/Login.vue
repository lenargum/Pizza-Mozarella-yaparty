<template>
  <NavPage :header="'Логин'" :username="username">
    <v-row
      justify="center" class="align-self-start">
      <v-col cols="11" sm="10" md="10" lg="4" xl="2" align-self="center">
        <v-text-field
          autofocus
          clearable
          :counter="10"
          :height="100"
          solo
          v-model="username"
          :maxlength="10"
        />
      </v-col>
      <v-col cols="3" sm="2" md="1" lg="1" xl="1" align-self="start">
        <SmallFab @click="$router.push('/home')" type="forward"/>
      </v-col>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";

export default {
  name: "Login",
  components: {SmallFab, NavPage},
  data: () => ({
    username: ""
  }),
}
</script>
<style scoped>
.app .v-input {
  font-size: 1.5em;
}
</style>