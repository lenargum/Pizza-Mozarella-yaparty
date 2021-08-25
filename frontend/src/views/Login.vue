<template>
  <NavPage :header="'Логин'" :username="username">
    <TextField>
      <template #default>
        <v-text-field
          autofocus
          clearable
          :counter="10"
          :height="100"
          solo
          v-model="username"
          :maxlength="10"
        />
      </template>
      <template #button>
        <SmallFab @click="$router.push('/home')" type="forward"/>
      </template>
    </TextField>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";

export default {
  name: "Login",
  components: {TextField, SmallFab, NavPage},
  data: () => ({
    username: ""
  }),
}
</script>