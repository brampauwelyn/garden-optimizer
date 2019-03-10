<template>
  <table v-if="list.length > 0">
    <caption>{{ title }}</caption>
    <tbody>
      <tr :key="key" v-for="(item,key) in list">
        <td>{{ item }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
  export default {
    name: 'Table',
    props: {
      title: String,
      list: Array
    }
  }
</script>

<style lang="scss" scoped>
table{
  border-collapse: collapse;
  width: 40%;
}

table,th,td{
  border: 1px solid black;
}

table caption{
  border-top: 1px solid black;
  border-left: 1px solid black;
  border-right: 1px solid black;
  padding: 10px;
  font-size: 1.2em;
  background-color: #26de81;
  font-weight: bold;
  color: #fff;
}

table td{
  padding: 10px;
}
</style>
