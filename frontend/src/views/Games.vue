<template>
  <NavPage>
    <div class="games">
      <h2 class="games__title text-h4 text-sm-h3 text-md-h2 text-lg-h2 text-xl-h1">
        Ваша библиотека
      </h2>
      <div class="games__tiles">
        <div @click="$router.push('/create/game')" class="games__tile">
          <Tile :hoverable="true" :label="'Угадай мелодию'"
                :img="'guess_the_melody'"/>
        </div>
        <div class="games__tile">
          <Tile :hoverable="true" :label="'Игра 2'"/>
        </div>
        <div class="games__tile">
          <Tile class="games__tile" :hoverable="true" :label="'Игра 3'"/>
        </div>
      </div>
      <h2 class="games__title text-h4 text-sm-h3 text-md-h2 text-lg-h2 text-xl-h1">
        Маркет
      </h2>
      <div class="games__tiles">
        <div class="games__tile">
          <Tile class="games__tile" :hoverable="true" :label="'Игра 4'" tile-color="#FC3F1D" text-color="#fff"/>
        </div>
        <div class="games__tile">
          <Tile class="games__tile" :hoverable="true" :label="'Игра 5'" tile-color="#FC3F1D" text-color="#fff"/>
        </div>
        <div class="games__tile">
          <Tile class="games__tile" :hoverable="true" :label="'Игра 6'" tile-color="#FC3F1D" text-color="#fff"/>
        </div>
      </div>
    </div>
  </NavPage>
</template>

<script>
import NavPage from "@/views/templates/NavPage";
import Tile from "@/components/Tile";

export default {
  name: "Games",
  components: {Tile, NavPage}
}
</script>

<style lang="scss" scoped>
.games {
  align-self: flex-start;
  margin: 3vh 4vw;

  &__title {
    max-width: 500px;
    font-weight: 500;
    margin-bottom: 40px;
  }

  &__tiles {
    display: flex;
    flex-direction: row;
    gap: 40px;
    flex-wrap: wrap;
    margin-bottom: 3vh;
  }

  &__tile {
    cursor: pointer;
    user-select: none;
  }
}

</style>