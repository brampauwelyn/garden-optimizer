<template>
  <div class="tag">
   <span>{{ text }}</span>
  </div>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    text: String
  }
}
</script>


<style lang="scss" scoped>
.tag{
  padding: 5px 10px;
  background-color: #dfe4ea;
  border-radius: 4px;
  display: inline-block;
  margin: 10px;
}
</style>
