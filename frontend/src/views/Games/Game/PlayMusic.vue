<template>
  <NavPage :header="'Угадай мелодию'">
    <v-row align="center"
           justify="center" class="align-self-start">
      <MusicPlayer/>
    </v-row>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import MusicPlayer from "@/components/MusicPlayer";

export default {
  name: "PlayMusic",
  components: {MusicPlayer, NavPage}
}
</script>

<style scoped>

</style>