<template>
  <NavPage :header="'Таблица очков'" :username="username">
    <v-row align="center"
           justify="center" class="align-self-start">
      <v-col align-self="center" class="leaderboard__wrapper">
        <v-data-table
          :headers="headers"
          :items="scoreboard"
          class="elevation-1 leaderboard__table"
          :disable-pagination="true"
          :disable-filtering="true"
          :disable-sort="true"
          :hide-default-footer="true"
          :fixed-header="true"
          :height="'50vh'"
          :mobile-breakpoint="0"
        />
        <SmallFab @click="$router.push('/');" :type="'home'"/>
      </v-col>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import SmallFab from "@/components/SmallFab";

export default {
  name: "LeaderBoard",
  components: {SmallFab, NavPage},
  props: {
    scoreboard: Array,
    username: String,
  },
  data: () => ({
    headers: [
      {text: 'Игрок', value: 'username'},
      {text: 'Очки', value: 'score'},
    ],
  }),
}
</script>

<style lang="scss" scoped>
.cover-wrapper {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.app {
  .leaderboard {
    &__table {
      margin: 10px;
      width: 50vw;
    }

    &__wrapper {
      justify-content: space-around;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }
  }
}
</style>