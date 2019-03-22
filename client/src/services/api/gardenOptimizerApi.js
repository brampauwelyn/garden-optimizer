import axios from 'axios';

export default{
  getPlants(){
    const url = 'http://localhost:5000/vegetables';
    return axios.get(url)
    .then((response) => {
      return response;
    });
  },
  getPlantInfo(plantid){
    const url = `http://localhost:5000/getplantinfo?plantid=${plantid}`;
    return axios.get(url)
    .then((response) => {
      return response;
    });
  }
}