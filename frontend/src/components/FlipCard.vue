<template>
  <div class="flip-card" :class="{'flip-card_turned': turned}">
    <div class="flip-card-inner" :class="{'flip-card-inner_turned': turned}">
      <div class="flip-card-front">
        <Tile :label="'???'" :img="'guess_the_melody'"/>
      </div>
      <div class="flip-card-back" :style="{'--answerColor': answerColor}">
        <h4 class="flip-card__track text-h6 text-sm-h5 text-md-h4 text-lg-h4 text-xl-h3">{{ track }}</h4>
        <h5 class="flip-card__artist text-h7 text-sm-h6 text-md-h5 text-lg-h5 text-xl-h4">{{ artist }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import Tile from "@/components/Tile";

export default {
  name: "FlipCard",
  components: {Tile},
  props: {
    track: String,
    artist: String,
    turned: {
      type: Boolean,
      default: false
    },
    answerColor: {
      type: String,
      default: "#FFCC00"
    }
  },
  data: () => ({}),
}
</script>

<style lang="scss" scoped>
.flip-card {
  background-color: transparent;
  width: 200px;
  height: 200px;
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

/* Do an horizontal flip when you move the mouse over the flip box container */


.flip-card_turned .flip-card-inner_turned {
  transform: rotateY(180deg);
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  background-color: $style_yellow;
  color: $style_black;
}

/* Style the back side */
.flip-card-back {
  background-color: var(--answerColor);
  color: $style_black;
  transform: rotateY(180deg);
}

.flip-card {
  &__track {
    width: 200px;
    height: 100px;
    overflow-wrap: break-word;

    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    filter: drop-shadow(0px 8.19231px 8.19231px rgba(0, 0, 0, 0.161));
  }

  &__artist {
    width: 200px;
    height: 100px;
    font-weight: bold;
    overflow-wrap: break-word;

    display: flex;
    flex-direction: column;
    justify-content: center;
    filter: drop-shadow(0px 8.19231px 8.19231px rgba(0, 0, 0, 0.161));
  }
}
</style>