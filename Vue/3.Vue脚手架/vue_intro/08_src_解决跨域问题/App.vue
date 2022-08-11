<template>
    <!--
        配置代理（修改 vue.config.js 中的 devServer 字段）
    -->
    <div>
        <button @click="getData">获取数据</button>
    </div>
</template>

<script>

    import axios from 'axios'

    export default {
        name: 'App',
        methods: {
            getData(){
                axios.get('http://localhost:8081/test/getJson').then(
                    success => {
                        console.log("获取数据成功", success.data)
                    },
                    failed => {
                        console.log("获取数据失败", failed.message)
                    }
                )
            }
        }
    }
</script>

<style>

</style>