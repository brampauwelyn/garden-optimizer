<template>
  <div>
    <h1>{{ $route.params.id }} {{officialName}}</h1>
    <img width="400" :src="plantImage" alt="">
    <div class="table-container">
      <Table title="❤️ Companion Plants" :list="selectedPlant.companion"/>
      <Table title="Antagonistic plants" :list="selectedPlant.antagonistic"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Table from '@/components/Table.vue';
export default {
  name: "Plant",
  components: {
    Table
  },
  data: function(){
    return {
      name: this.$route.params.id,
      allPlants: "",
      selectedPlant: "",
      plantId: "",
      officialName: "",
      plantImage: ""
    }
  },
  watch: {
    // call again the methods if the route changes
    '$route': ['getPlant', 'getPlantInfo']
  },
  methods: {
    getPlant: function(){
      const url = 'http://localhost:5000/vegetables';
      axios.get(url)
      .then((res) => {
        this.allPlants = res.data.vegetables;
        this.selectedPlant = this.allPlants.filter(plant => plant.name === this.$route.params.id)[0];
      });
    },
    getPlantInfo: function(){
      const url = `http://localhost:5000/getplant?name=${this.name}`;
      axios.get(url)
      .then((res) => {
        this.officialName = res.data.scientific_name;
        this.plantImage = res.data.images[0].url;
      })
      .catch((error) => {
        console.log('show me the error: ' + error);
      });
    }
  },
  created(){
    this.getPlant();
    this.getPlantInfo();
  }
}
</script>


<style lang="scss" scoped>
  .table-container{
    display: flex;
    justify-content: space-around;
  }
</style>
