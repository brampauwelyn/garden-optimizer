import axios from 'axios';

export default{
  getPlants(){
    const url = 'http://localhost/vegetables';
    return axios.get(url)
    .then((response) => {
      return response;
    });
  },
  getPlantInfo(plantid){
    const url = `http://localhost/getplantinfo?plantid=${plantid}`;
    return axios.get(url)
    .then((response) => {
      return response;
    });
  }
}