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
        <SmallFab @click="loginHandler" type="forward"/>
      </template>
    </TextField>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";
import TextField from "@/components/TextField";

export default {
  name: "MobileLogin",
  components: {TextField, SmallFab, NavPage},
  data: () => ({
    username: "",
    sessionId: "",
    ws: null
  }),
  methods: {
    loginHandler() {
      this.connect();
      // this.$router.push('/play');
    },

  },
  mounted() {
    this.sessionId = this.$route.params.sessionId;
  }
}
</script>