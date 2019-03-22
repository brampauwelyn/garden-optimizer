<template>
  <div class="home">
    <h1>Garden Optimizer</h1>
     <div>
      <Tag :key="key" v-for="(veggie,key) in selectedVeggies" :text="veggie" @removeTag="removeVeggie(veggie)"/>
        <Button v-if="selectedVeggies.length > 1">Start the magic</Button>
    </div>
    <div class="suggest-container">
      <input @input="searchSuggestions" v-model="searchQuery" placeholder="Which plants do you want to grow?" class="search-field" type="text">
      <ul class="suggest-box" v-show="focusActive">
        <li :key="key" v-for="(result ,key) in searchResults" @click="addVeggie(result.name)">
         {{ result.name }}
          <router-link :to="{ name: 'plant', params: { id: result.name }}">detail</router-link>
        </li>
      </ul>
    </div>

    <img src="@/assets/Vegetables-Garden.jpg" style="display:block;margin:0 auto;" width="800" alt="">
  </div>
</template>

<script>
// @ is an alias to /src
import Tag from '@/components/Tag.vue';
import Button from '@/components/Button.vue';
import gardenOptimizerApi from '@/services/api/gardenOptimizerApi';

export default {
  name: 'home',
  components: {
    Tag,
    Button
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
      gardenOptimizerApi.getPlants()
      .then(plants => {
        this.suggestions = plants.data.vegetables;
      })
    },
    searchSuggestions:  function(){
      if(this.searchQuery.length > 0){
        this.searchResults = [];
        this.searchResults = this.suggestions.filter(suggestion => suggestion.name.toLowerCase().indexOf(this.searchQuery.toLowerCase())> -1);
        this.focusActive =  (this.searchResults.length > 0) ? true : false;
      }else{
        this.focusActive = false;
      }
    },
    addVeggie: function(veggie){
      this.selectedVeggies.push(veggie);
      this.focusActive = false;
    },
    removeVeggie: function(veggie){
      if(this.selectedVeggies.indexOf(veggie) > -1){
        this.selectedVeggies.splice(veggie, 1);
      }
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
