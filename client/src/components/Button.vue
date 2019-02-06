<template>
    <button class="button__primary">
      <slot></slot>  
    </button> 
</template>


<script>
export default {
  name: 'Button'
}
</script>

<style lang="scss" scoped>
  .button__primary{
    background-color: darken(#5AA8FB, 10%);
    padding: 15px 20px; 
    font-size: 1.2em;
    border: 0;
    border-radius: 50px;
    color: #fff;
    cursor: pointer;
    animation: fadein 2s;
    transition: background-color .25s;
  }

  .button__primary:hover{
    background-color: darken(#5AA8FB,20%);
  }

@keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

</style>
