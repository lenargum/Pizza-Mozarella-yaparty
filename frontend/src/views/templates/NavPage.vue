<template>
  <div>
    <v-navigation-drawer v-if="hasDrawer"
                         v-model="drawer"
                         app
    >
      <div class="drawer-wrapper">
        <Link :to="'/'">
          /
        </Link>
        <Link v-for="(route, index) in $router.getRoutes()" :to="route.path" :key="index">
          {{ route.path }}
        </Link>
      </div>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon v-if="hasDrawer" @click="drawer = !drawer"></v-app-bar-nav-icon>
      <div class="navbar-wrapper">
        <Link to="/">
          <Logo/>
        </Link>
        <slot name="username"/>
      </div>
    </v-app-bar>

    <v-main>
      <slot name="default"/>
    </v-main>
  </div>
</template>

<script>
import Link from "@/components/Link";
import Logo from "@/components/Icons/Logo";

export default {
  name: "NavPage",
  components: {Logo, Link},
  props: {
    hasDrawer: {
      type: Boolean,
      default: true
    }
  },
  data: () => ({
    drawer: false,
  }),
}
</script>

<style lang="scss" scoped>
.app {
  .navbar-wrapper {
    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0 40px;
  }

  .drawer-wrapper {
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
    align-items: flex-start;
    padding: 50px 50px;
    gap: 10px;

    overflow-y: auto;
  }
}
</style>