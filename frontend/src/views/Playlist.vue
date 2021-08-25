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
        :fixed-header="true"
        :height="'70vh'"
        :loading="loading"
        loading-text="Загрузка..."
      >
        <template #item.track_cover="{item}">
          <div class="cover-wrapper" :style="{width: 32, height: 32}">
            <img :src="item.track_cover.url" :style="{maxWidth: '100%', maxHeight: '100%'}" alt=""/>
          </div>
        </template>
        <template #item.duration_ms="{item}">
          {{ millisToMinutesAndSeconds(item.duration_ms) }}
        </template>
        <template #item.artists="{item}">
          {{ item.artists.toString() }}
        </template>
      </v-data-table>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";

export default {
  name: "Playlist",
  components: {NavPage},
  data: () => ({
    headers: [
      {text: 'Обложка', value: 'track_cover'},
      {text: 'Название', value: 'track_name'},
      {text: 'Исполнитель', value: 'artists'},
      {text: 'Длительность', value: 'duration_ms'},
    ],
    tableData: [],
    roomId: '',
    loading: true
  }),
  methods: {
    millisToMinutesAndSeconds(millis) {
      const minutes = Math.floor(millis / 60000);
      const seconds = ((millis % 60000) / 1000).toFixed(0);
      return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }
  },
   async created() {
     this.roomId = this.$route.params.id;

     const requestOptions = {
       method: "GET",
       headers: {"Content-Type": "application/json"},
     };
     try {
       const response = await fetch("https://secure-ridge-64426.herokuapp.com/http://84.201.167.68:8000/recommend?room_id=" + this.roomId + "&size=30", requestOptions);
       const data = await response.json();
       this.tableData = data;
       this.loading = false;
     } catch (e) {
       this.loading = false;
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