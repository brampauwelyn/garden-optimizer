<template>
  <div>
    <PlantImage v-if="plantImage" :image="plantImage"/>
    <h1>{{ $route.params.id }}</h1>
    <h3 v-if="officialName">({{ officialName }})</h3>
    <div class="table-container">
      <Table title="❤️ Companion Plants" :list="selectedPlant.companion"/>
      <Table title="Antagonistic plants" :list="selectedPlant.antagonistic"/>
    </div>
  </div>
</template>

<script>
import gardenOptimizerApi from '@/services/api/gardenOptimizerApi';
import PlantImage from '@/components/PlantImage.vue';
import Table from '@/components/Table.vue';
export default {
  name: "Plant",
  components: {
    PlantImage,
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
    '$route': 'getPlantInfo'
  },
  methods: {
    getAllPlants: function(){
      return gardenOptimizerApi.getPlants()
      .then(plants => {
        this.allPlants = plants.data.vegetables;
        this.selectedPlant = this.allPlants.filter(plant => plant.name === this.$route.params.id)[0];
      })
    },
    getPlantInfo: function(){
      this.selectedPlant = this.allPlants.filter(plant => plant.name === this.$route.params.id)[0];
      this.plantId = this.selectedPlant.trefle_id;
      gardenOptimizerApi.getPlantInfo(this.plantId)
      .then(plant => {
        this.officialName = plant.data.scientific_name;
        this.plantImage = plant.data.images[0].url;
      })
      .catch(() => {
        this.officialName = "";
        this.plantImage = "";
      })
    }
  },
  created(){
    this.getAllPlants().then( () => this.getPlantInfo());
  }
}
</script>


<style lang="scss" scoped>
  .table-container{
    display: flex;
    justify-content: space-around;
  }

  h1{
    text-transform: capitalize;
  }

  h3{
    font-style: italic;
    font-family: 'Georgia', serif;
  }
</style>
