<template>
  <div>
    <h2>我是Home页面</h2>
    <div>
      <router-link class="unactive" active-class="active" to="/home/news">news</router-link>
      <router-link class="unactive" active-class="active" to="/home/message">message</router-link>
    </div>
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  export default {
      name: 'Home'
  }
</script>

<style>

</style>