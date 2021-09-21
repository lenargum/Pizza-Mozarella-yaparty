<template>
  <div class="pacman-wrapper" :style="{'--pacman-size': size.toString() + sizeUnit}">
    <PacmanLoader :color="color"
                  :size="size"
                  :sizeUnit="sizeUnit"
                  :style="{
                    transform: 'translate(-' + (size*2).toString() + sizeUnit + ', -' + size.toString() + sizeUnit + ')'
                  }"
    />
  </div>
</template>

<script>
import {PacmanLoader} from '@saeris/vue-spinners'

export default {
  name: "WaitingLoader",
  components: {
    PacmanLoader
  },
  props: {
    color: {
      type: String,
      default: '#FFCC00'
    }
  },
  data: () => ({
    size: 5,
    sizeUnit: 'vw'
  }),
}
</script>

<style lang="scss" scoped>
.pacman-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(var(--pacman-size) * 2);
  width: calc(var(--pacman-size) * 4);
}
</style>