<template>
  <div class="home">
    <h1>Garden Optimizer</h1>
    <Tag :key="key" v-for="(veggie,key) in selectedVeggies" :text="veggie" />
    <div class="suggest-container">
      <input @input="searchSuggestions" v-model="searchQuery" class="search-field" type="text">
      <ul class="suggest-box" v-show="focusActive">
        <li :key="key" v-for="(result ,key) in searchResults" @click="addVeggie(result)">
         {{ result }}
        </li>
      </ul>
    </div>
    <img src="@/assets/Vegetables-Garden.jpg" style="display:block;margin:0 auto;" width="800" alt="">
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import Tag from '@/components/Tag.vue';

export default {
  name: 'home',
  components: {
    Tag
  },
  data: function(){
    return{
      suggestions: [],
      searchQuery: '',
      searchResults: [],
      selectedVeggies: [],
      focusActive: false
    }
  },
  methods: {
    getAllVeggies: function(){
      const url = 'http://localhost:5000/vegetables';
      axios.get(url)
      .then( (res) => {
        console.log(res.data.vegetables);
        this.suggestions = res.data.vegetables;
      })
    },
    searchSuggestions:  function(){
      this.searchResults = [];
      this.searchResults = this.suggestions.filter(suggestion => suggestion.toLowerCase().indexOf(this.searchQuery.toLowerCase())> -1);
      this.focusActive = (this.searchResults.length) ? true : false;
    },
    addVeggie: function(veggie){
      this.selectedVeggies.push(veggie);
      this.focusActive = false;
    }
  },
  created(){
    this.getAllVeggies()
  }
}
</script>

<style lang="scss">
.search-field{
  width: calc(50%);
  height: 30px;
  padding:10px 15px;
  border-radius: 5px;
  border:1px solid darken(#5AA8FB, 10%);
  font-size: 1.1em;
}

.search-field:focus{
  border:1px solid #5AA8FB;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

.suggest-container{
  position: relative;
}

.suggest-box{
  position: absolute;
  width: calc(50% + 30px);
  left: calc(25% - 16px);
  padding-left: 0;
  margin: 0;
  border: 1px solid #5AA8FB;
  border-top: none;
  list-style: none;
}

.suggest-box li{
  padding: 8px;
  text-align: left;
  background-color: #fff;
}

.suggest-box li:hover{
  background-color: #5AA8FB;
  color: #fff;
}

</style>
