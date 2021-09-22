<template>
  <div class="music-player__wrapper">
    <div class="music-player">
      <svg :class="{'rotating': rotating}" width="399" height="399" viewBox="0 0 399 399" fill="none"
           xmlns="http://www.w3.org/2000/svg">
        <g filter="url(#filter0_d)">
          <circle cx="199.5" cy="199.5" r="179.5" fill="#222222"/>
          <circle cx="199.5" cy="199.5" r="179.5" stroke="white" stroke-width="10.77"/>
        </g>
        <circle cx="199.5" cy="199.5" r="39.5" fill="#F6F5F3" stroke="white" stroke-width="10.77"/>
        <mask id="mask0" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="165" y="166" width="69" height="69">
          <circle cx="199.105" cy="200.105" r="34.105" fill="#0054B9"/>
        </mask>
        <g mask="url(#mask0)">
          <g filter="url(#filter1_d)">
            <path
              d="M199.105 130.1C159.533 130.1 129.1 160.533 129.1 200.105C129.1 239.677 159.533 270.11 199.105 270.11C238.677 270.11 269.11 239.677 269.11 200.105C269.11 160.533 238.677 130.1 199.105 130.1Z"
              stroke="black" stroke-width="71.8"/>
          </g>
        </g>
        <mask id="mask1" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="199" y="82" width="119" height="119">
          <rect x="199" y="82" width="118.47" height="118.47" fill="#C4C4C4"/>
        </mask>
        <g mask="url(#mask1)">
          <circle cx="199.188" cy="200.188" r="106.802" stroke="white" stroke-width="10.77"/>
        </g>
        <mask id="mask2" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="81" y="200" width="119" height="119">
          <rect x="81" y="200" width="118.47" height="118.47" fill="#C4C4C4"/>
        </mask>
        <g mask="url(#mask2)">
          <circle cx="199.188" cy="200.188" r="106.802" stroke="white" stroke-width="10.77"/>
        </g>
        <defs>
          <filter id="filter0_d" x="0.254991" y="0.255235" width="398.49" height="398.49" filterUnits="userSpaceOnUse"
                  color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                           result="hardAlpha"/>
            <feOffset/>
            <feGaussianBlur stdDeviation="7.18"/>
            <feComposite in2="hardAlpha" operator="out"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>
          </filter>
          <filter id="filter1_d" x="82.43" y="83.4302" width="233.35" height="233.35" filterUnits="userSpaceOnUse"
                  color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                           result="hardAlpha"/>
            <feOffset/>
            <feGaussianBlur stdDeviation="5.385"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>
          </filter>
        </defs>
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "MusicPlayer",
  props: {
    rotating: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="scss" scoped>
.music-player {
  width: 388px;
  height: 388px;
  line-height: 388px;
  text-align: center;

  &__wrapper {
    width: 420px;
    height: 420px;
    overflow: hidden;
  }
}

@-webkit-keyframes rotating /* Safari and Chrome */
{
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.rotating {
  -webkit-animation: rotating 2s linear infinite;
  -moz-animation: rotating 2s linear infinite;
  -ms-animation: rotating 2s linear infinite;
  -o-animation: rotating 2s linear infinite;
  animation: rotating 2s linear infinite;
}
</style>