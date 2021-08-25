<template>
  <div class="stub">
    <div class="stub_imgs">
      <img @click="$router.back()" class="stub__img" :src="require('@/assets/stub.jpg')" alt="">
      <img @click="$router.back()" class="stub__img stub__img_2" height="" :src="require('@/assets/stub2.jpg')" alt="">
    </div>
    <div class="stub__label">В разработке</div>
  </div>
</template>

<script>
export default {
  name: "Stub"
}
</script>

<style lang="scss" scoped>
.stub {
  display: flex;
  justify-content: center;
  align-items: center;

  &__img {
    transition: top 1s ease-in-out, left 1s ease-in-out, width 0.5s ease-in-out, height 0.5s ease-in-out;
    position: relative;
    width: 600px;
    height: 578px;

    &_2 {
      transition: top 1s ease-in-out, left 1s ease-in-out, width 0.5s ease-in-out, height 0.5s ease-in-out;
      position: relative;
      width: 600px;
      height: 400px;

      &:hover {
        width: 610px;
        height: 410px;
        top: -5px;
        left: -5px;
      }
    }

    &:hover {
      width: 610px;
      height: 588px;
      top: -5px;
      left: -5px;
    }
  }

  &__imgs {
    display: flex;
    justify-content: space-between;
  }

  &__label {
    position: absolute;
    top: 75%;
    left: 50%;
    text-align: center;
    transform: translate(-50%, -50%);

    font-family: $body-font-family;
    color: $style_black;
    font-weight: 700;
    font-size: 34px;
    line-height: 18px;
  }
}
</style>