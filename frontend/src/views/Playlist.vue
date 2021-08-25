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
      {
        "track_name": "Marimba",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485162f4a39c436a0cc45b727946",
          "height": 64,
          "width": 64
        },
        "duration_ms": 204096,
        "artists": [
          "Julian Lamadrid"
        ]
      },
      {
        "track_name": "Jiraiya",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485172dac1e81cc55f1dd99fff73",
          "height": 64,
          "width": 64
        },
        "duration_ms": 178673,
        "artists": [
          "NKOHA"
        ]
      },
      {
        "track_name": "Родной",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d00004851c642f3a5b5cb6f1b5fb62285",
          "height": 64,
          "width": 64
        },
        "duration_ms": 218332,
        "artists": [
          "Чёрный Государь"
        ]
      },
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
      {
        "track_name": "Marimba",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485162f4a39c436a0cc45b727946",
          "height": 64,
          "width": 64
        },
        "duration_ms": 204096,
        "artists": [
          "Julian Lamadrid"
        ]
      },
      {
        "track_name": "Jiraiya",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485172dac1e81cc55f1dd99fff73",
          "height": 64,
          "width": 64
        },
        "duration_ms": 178673,
        "artists": [
          "NKOHA"
        ]
      },
      {
        "track_name": "Родной",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d00004851c642f3a5b5cb6f1b5fb62285",
          "height": 64,
          "width": 64
        },
        "duration_ms": 218332,
        "artists": [
          "Чёрный Государь"
        ]
      },
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
      {
        "track_name": "Marimba",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485162f4a39c436a0cc45b727946",
          "height": 64,
          "width": 64
        },
        "duration_ms": 204096,
        "artists": [
          "Julian Lamadrid"
        ]
      },
      {
        "track_name": "Jiraiya",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d0000485172dac1e81cc55f1dd99fff73",
          "height": 64,
          "width": 64
        },
        "duration_ms": 178673,
        "artists": [
          "NKOHA"
        ]
      },
      {
        "track_name": "Родной",
        "track_cover": {
          "url": "https://i.scdn.co/image/ab67616d00004851c642f3a5b5cb6f1b5fb62285",
          "height": 64,
          "width": 64
        },
        "duration_ms": 218332,
        "artists": [
          "Чёрный Государь"
        ]
      }
    ],
    roomId: ''
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
       headers: { "Content-Type": "application/json" },
     };
     const response = await fetch("https://secure-ridge-64426.herokuapp.com/http://84.201.167.68:8000/recommend?room_id="+this.roomId+"&size=30", requestOptions);
     const data = await response.json();
     this.tableData = data;
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