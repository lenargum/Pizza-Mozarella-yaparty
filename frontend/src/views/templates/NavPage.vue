<template>
  <v-app>
    <v-navigation-drawer v-if="hasDrawer"
                         v-model="drawerIsOpen"
                         app
    >
      <div class="drawer-wrapper">
        <Link :to="'/'">
          /
        </Link>
        <Link v-for="(route, index) in $router.getRoutes()" :to="route.path" :key="index">
          {{ route.path }}
        </Link>
        <hr style="width:100%">
        <slot name="debug"/>
      </div>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon v-if="hasDrawer" @click="drawerIsOpen = !drawerIsOpen" title="Debug"/>
      <div class="navbar-wrapper">
        <Link to="/">
          <Logo/>
        </Link>
        <template v-if="username">
          <h5 class="text-h7 text-sm-h6 text-md-h6 text-lg-h5 text-xl-h4">{{ username }}</h5>
        </template>
      </div>
    </v-app-bar>

    <v-main>
      <v-container fill-height fluid>
        <CurrentUsers v-if="users" :users="users"/>
        <Score v-if="score" :score="score"/>
        <HeaderTitle v-if="header">{{ header }}</HeaderTitle>
        <slot name="default"/>

      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Link from "@/components/Link";
import Logo from "@/components/Icons/Logo";
import CurrentUsers from "@/components/CurrentUsers";
import Score from "@/components/Score";
import HeaderTitle from "@/components/HeaderTitle";

export default {
  name: "NavPage",
  components: {HeaderTitle, Score, CurrentUsers, Logo, Link},
  props: {
    users: {
      type: Array,
      default: undefined
    },
    username: {
      type: String,
      default: undefined
    },
    score: {
      type: String,
      default: undefined
    },
    header: {
      type: String,
      default: undefined
    }
  },
  data: () => ({
    drawerIsOpen: false,
    hasDrawer: false
  }),
  mounted() {
    this.hasDrawer = process.env.NODE_ENV === 'development';
  }
}
</script>

<style lang="scss" scoped>
.app {
  .navbar-wrapper {
    width: 100%;
    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0 0.02vw;
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

  .page-wrapper {
    height: 100vh;
    width: 100vw;
  }
}
</style>