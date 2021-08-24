<template>
  <div class="users__wrapper">
    <div class="users__label">Участники:</div>
    <div v-for="(user, index) in users" class="users__user" :key="index">{{ user }}</div>
  </div>
</template>

<script>
export default {
  name: "CurrentUsers",
  props: {
    users: Array,
  }
}
</script>

<style lang="scss" scoped>
.users {
  &__wrapper {
    position: absolute;
    top: 10px;
    right: 10px;

    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;

  }
}
</style>