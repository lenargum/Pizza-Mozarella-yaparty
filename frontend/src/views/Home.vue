<template>
  <Page :style="'background-color: fff;'">
    <div class="page__wrapper">
      <div class="page__logo">
        <Logo :is-black="false"/>
      </div>
      <div class="page__content">
        <div @click="navigateToStub" class="page__service">
          <Tile :hoverable="true" :label="'Афиша'" :img="'afisha'" :tile-color="'#FFCC00'"/>
          <span class="page__service-text">
            Найдём мероприятие
          </span>
        </div>

        <div @click="$router.push('/playlist/'+this.roomId)" class="page__service">
          <Tile :hoverable="true" :label="'Плейлист вечеринки'" :img="'party-playlist'"
                :tile-color="'#6DAAE8'"/>
          <span class="page__service-text">
            Соберём плейлист
          </span>
        </div>

        <div @click="navigateToStub" class="page__service">
          <Tile :hoverable="true" :label="'Еда'" :img="'eda'" :tile-color="'#FFCC00'"/>
          <span class="page__service-text">
            Организуем закуски
          </span>
        </div>

        <div @click="navigateToStub" class="page__service">
          <Tile :hoverable="true" :label="'Кино'" :img="'kino'" :text-color="'#fff'"
                :tile-color="'#777'"/>
          <span class="page__service-text">
            Подскажем, что посмотреть
          </span>
        </div>

        <div @click="$router.push('/games')" class="page__service">
          <Tile :hoverable="true" :label="'Игры'" :img="'games'" :text-color="'#fff'"
                :tile-color="'#FC3F1D'"/>
          <span class="page__service-text">
            Не дадим заскучать
          </span>
        </div>
      </div>
    </div>
  </Page>
</template>

<script>
import Tile from "@/components/Tile";
import Page from "@/views/templates/Page";
import Logo from "@/components/Icons/Logo";

export default {
  name: "Home",
  components: {Logo, Page, Tile},
  data: () => ({
    roomId: ''
  }),
  methods: {
    navigateToStub() {
      this.$router.push('/in-progress');
    }
  },
  mounted() {
    this.roomId = this.$route.params.id;
  }
}
</script>

<style lang="scss" scoped>
.page {
  &__wrapper {
    position: relative;
    background-image: url("/static/disco.png");
    background-size: cover;

    width: 100vw;
    height: 100vh;

    display: flex;
    flex-wrap: nowrap;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  &__logo {
    position: absolute;
    top: 50px;
    left: 50px;
  }

  &__content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-between;
    gap: 10px;

    padding: 0 5%;
  }

  &__service {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 35px;

    cursor: pointer;

    &-text {
      width: 200px;

      font-family: $body-font-family;
      font-style: normal;
      font-weight: bold;
      font-size: 30px;
      line-height: 34px;
      text-align: center;

      color: #FFFFFF;

      text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    }
  }
}
</style>