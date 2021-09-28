<template>
  <div class="users__wrapper">
    <div class="users__label text-h8 text-sm-h7 text-md-h7 text-lg-h6 text-xl-h5 font-weight-bold">Участники:</div>
    <div v-for="(user, index) in users" class="users__user text-h8 text-sm-h7 text-md-h7 text-lg-h6 text-xl-h5"
         :key="index">
      <template v-if="user === judge">
        <p class="users__user_judge">{{ user }}</p>
      </template>
      <template v-else>
        {{ user }}
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: "CurrentUsers",
  props: {
    users: Array,
    judge: {
      type: String,
      default: ''
    },
  }
}
</script>

<style lang="scss" scoped>
.app p {
  margin-bottom: 0;
}

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

  &__user {

    &_judge {
      background-color: #FFCC00;
    }
  }
}

@media (max-width: 500px) {
  .users {
    &__label {
      display: none;
    }

    &__wrapper {
      top: 50px;
    }
  }

}
</style>