<template>
  <NavPage :header="'Общий плейлист'">
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
        :height="'70vh'"
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
        "track_name": "Another World",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485163ef64fbbaed7ae560aae0a5",
          "height": 64,
          "width": 64
        },
        "duration_ms": 271807,
        "artists": [
          "plenka"
        ]
      },
      {
        "track_name": "Тайна",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d000048518c00a9564293be7d830a43e0",
          "height": 64,
          "width": 64
        },
        "duration_ms": 181510,
        "artists": [
          "Увула"
        ]
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
  }
}
</style>