<template>
  <div class="plant__image">
    <img :src="image" alt="">
  </div>
</template>


<script>
export default {
  name: 'PlantImage',
  props: {
    image: String
  }
}
</script>

<style lang="scss" scoped>
 .plant__image{
    margin: 0 auto;
    width: 200px;
    height: 200px;
    overflow: hidden;
    border-radius: 50%;

    img{
      width: 150%;
    }
  }
</style>
