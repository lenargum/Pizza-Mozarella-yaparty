<template>
  <NavPage :header="'Таблица очков'">
    <v-row align="center"
           justify="center" class="align-self-start">
      <v-data-table
        :headers="headers"
        :items="tableData"
        class="elevation-1 playlist__table"
        :disable-pagination="true"
        :disable-filtering="true"
        :disable-sort="true"
        :hide-default-footer="true"
        :fixed-header="true"
      >
        <template #item.track_cover="{item}">
          <div class="cover-wrapper" :style="{width: 32, height: 32}">
            <img :src="item.track_cover.url" :style="{maxWidth: '100%', maxHeight: '100%'}" alt=""/>
          </div>
        </template>
        <template #item.duration_ms="{item}">
          {{ millisToMinutesAndSeconds(item.duration_ms) }}
        </template>
      </v-data-table>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";

export default {
  name: "LeaderBoard",
  components: {NavPage},
  data: () => ({
    headers: [
      {text: 'Игрок', value: 'username'},
      {text: 'Очки', value: 'score'},

    ],
    tableData: [
      {
        username: 'Игрок 1', score: 100
      },
      {
        username: 'Игрок 2', score: 200
      },
      {
        username: 'Игрок 1', score: 100
      },
      {
        username: 'Игрок 2', score: 200
      },
      {
        username: 'Игрок 1', score: 100
      },
      {
        username: 'Игрок 2', score: 200
      },
    ]
  }),
  methods: {
    millisToMinutesAndSeconds(millis) {
      console.log(millis);
      const minutes = Math.floor(millis / 60000);
      const seconds = ((millis % 60000) / 1000).toFixed(0);
      return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }
  }

}
</script>

<style lang="scss" scoped>
.cover-wrapper {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.app {
  .playlist__table {
    margin: 10px;
    width: 50vw;
    max-height: 70vh;
  }
}
</style>