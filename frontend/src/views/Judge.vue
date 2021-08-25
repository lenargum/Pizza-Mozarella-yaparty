<template>
  <NavPage :username="login" :users="users">
    <h1 style="text-align: center">{{ $options.name }}</h1>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";

export default {
  name: "Judge",
  components: {NavPage},
  data: () => ({
    login: 'username stub',
    users: [
      'stub1',
      'stub2'
    ],
  }),
  methods: {
    setUsers(users) {
      this.users = users;
    },
    setLogin(login) {
      this.login = login;
    },
  }
}
</script>

<style scoped>

</style>