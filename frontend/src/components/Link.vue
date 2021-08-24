<template>
  <router-link :to="to" class="pizza__link">
    <slot/>
  </router-link>
</template>

<script>
export default {
  name: "Link",
  props: {
    to: String,
  }
}
</script>

<style lang="scss" scoped>
.app {
  .pizza {
    &__link {
      line-height: 1;
      font-weight: bold;
      color: $style_light-blue;

      &.router-link-exact-active {
        color: $style_blue;
      }
    }
  }
}
</style>