<template>
  <div class="tag">
   <span>{{ text }}</span>
   <button @click="removeTag" class="tag__remove"></button>
  </div>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    text: String
  },
  methods: {
    removeTag: function(){
      this.$emit('removeTag');
    }
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
  animation: fadein 1s;
}

.tag__remove{
  -moz-appearance: none;
  -webkit-appearance: none;
  background-color: rgba(10,10,10,.2);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  pointer-events: auto;
  display: inline-block;
  height: 20px;
  max-height: 20px;
  max-width: 20px;
  min-height: 20px;
  min-width: 20px;
  outline: 0;
  position: relative;
  vertical-align: top;
  width: 20px;
  margin-left: 10px;
}

.tag__remove:hover{
  background-color: rgba(10,10,10,.3);
}

.tag__remove::before,
.tag__remove::after{
    height: 2px;
  width: 50%;
  background-color: #fff;
  content: "";
  display: block;
  left: 50%;
  position: absolute;
  top: 50%;
}

.tag__remove::before{
  -webkit-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  transform: translateX(-50%) translateY(-50%) rotate(45deg);
}

.tag__remove::after{
   -webkit-transform: translateX(-50%) translateY(-50%) rotate(45deg);
  transform: translateX(-50%) translateY(-50%) rotate(-45deg);
}


@keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

</style>
