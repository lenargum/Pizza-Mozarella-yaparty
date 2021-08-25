<template>
  <div class="users__wrapper">
    <div class="users__label text-h8 text-sm-h7 text-md-h7 text-lg-h6 text-xl-h5 font-weight-bold">Участники:</div>
    <div v-for="(user, index) in users" class="users__user text-h8 text-sm-h7 text-md-h7 text-lg-h6 text-xl-h5"
         :key="index">{{ user }}
    </div>
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

@media (max-width: 500px) {
  .users__label {
    display: none;
  }
}
</style>