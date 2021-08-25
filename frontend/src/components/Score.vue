<template>
  <div class="score__wrapper">
    <div class="score__label text-h8 text-sm-h7 text-md-h6 text-lg-h6 text-xl-h5">Очки:</div>
    <div class="score__value text-h7 text-sm-h6 text-md-h5 text-lg-h5 text-xl-h4">{{ score }}</div>
  </div>
</template>

<script>
export default {
  name: "Score",
  props: {
    score: String
  },
}
</script>

<style lang="scss" scoped>
.score {
  &__wrapper {
    position: absolute;
    left: 50%;
    bottom: 2vh;
    text-align: center;
    transform: translate(-50%, -50%);

    //margin: 0 auto;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  &__label {
    font-weight: bold;
  }

  &__value {

  }
}
</style>