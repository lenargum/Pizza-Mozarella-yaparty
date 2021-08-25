<template>
  <div
    class="music-player"
    :class="{'rotating': rotating}"
    style="width: 388px; height: 388px; line-height: 388px; text-align: center;"
  >
    <svg width="388" height="388" viewBox="0 0 388 388" fill="none" xmlns="http://www.w3.org/2000/svg">
      <g filter="url(#filter0_d)">
        <circle cx="194.5" cy="179.5" r="179.5" fill="#222222"/>
        <circle cx="194.5" cy="179.5" r="174.115" stroke="white" stroke-width="10.77"/>
      </g>
      <circle cx="192.705" cy="177.705" r="39.49" fill="#F6F5F3" stroke="white" stroke-width="10.77"/>
      <mask id="mask0" mask-type="alpha" maskUnits="userSpaceOnUse" x="158" y="143" width="69" height="69">
        <circle cx="192.705" cy="177.705" r="34.105" fill="#0054B9"/>
      </mask>
      <g mask="url(#mask0)">
        <g filter="url(#filter1_d)">
          <path
            d="M192.705 107.7C153.133 107.7 122.7 138.133 122.7 177.705C122.7 217.277 153.133 247.71 192.705 247.71C232.277 247.71 262.71 217.277 262.71 177.705C262.71 138.133 232.277 107.7 192.705 107.7Z"
            stroke="black" stroke-width="71.8"/>
        </g>
      </g>
      <mask id="mask1" mask-type="alpha" maskUnits="userSpaceOnUse" x="192" y="59" width="120" height="119">
        <rect x="192.705" y="59.2349" width="118.47" height="118.47" fill="#C4C4C4"/>
      </mask>
      <g mask="url(#mask1)">
        <circle cx="195.397" cy="180.397" r="106.802" stroke="white" stroke-width="10.77"/>
      </g>
      <mask id="mask2" mask-type="alpha" maskUnits="userSpaceOnUse" x="74" y="177" width="119" height="120">
        <rect x="74.235" y="177.705" width="118.47" height="118.47" fill="#C4C4C4"/>
      </mask>
      <g mask="url(#mask2)">
        <circle cx="195.397" cy="180.397" r="106.802" stroke="white" stroke-width="10.77"/>
      </g>
      <defs>
        <filter id="filter0_d" x="0.64" y="0" width="387.72" height="387.72" filterUnits="userSpaceOnUse"
                color-interpolation-filters="sRGB">
          <feFlood flood-opacity="0" result="BackgroundImageFix"/>
          <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                         result="hardAlpha"/>
          <feOffset dy="14.36"/>
          <feGaussianBlur stdDeviation="7.18"/>
          <feComposite in2="hardAlpha" operator="out"/>
          <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
          <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>
          <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>
        </filter>
        <filter id="filter1_d" x="76.0299" y="71.8003" width="233.35" height="233.35" filterUnits="userSpaceOnUse"
                color-interpolation-filters="sRGB">
          <feFlood flood-opacity="0" result="BackgroundImageFix"/>
          <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                         result="hardAlpha"/>
          <feOffset dy="10.77"/>
          <feGaussianBlur stdDeviation="5.385"/>
          <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
          <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow"/>
          <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow" result="shape"/>
        </filter>
      </defs>
    </svg>
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