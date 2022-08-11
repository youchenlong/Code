<template>
    <!--
        vue-router

        vue-link 渲染为a标签
        vue-view 渲染匹配到的组件
    -->

    <div class="container">
        <div class="header">
            <router-link class="unactive" active-class="active" to="/home">Home</router-link>
            <router-link class="unactive" active-class="active" to="/about">About</router-link>
        </div>
        <div class="body">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'App',
    }
</script>

<style>
    .container{
        display: flex;
        flex-direction: column;
        padding: 10px;
    }
    .header{
        border-style: solid;
        border-color: green;
        text-align: center;
        margin: 5px;
        padding: 5px;
    }
    .body{
        border-style: solid;
        border-color: blue;
        margin: 5px;
        text-align: center;
    }
    .unactive{
        text-decoration: none;
        border-style: solid;
        border-color: green;
        margin: 10px;
        padding: 1px;
    }
    .active{
        background-color: yellowgreen;
    }
</style>