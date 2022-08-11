<template>
    <div class="demo">
        <h2>{{name}}</h2>
        <h2>{{address}}</h2>
    </div>
</template>

<script>
    export default {
        name: 'School',
        data(){
            return{
                name: "尚硅谷",
                address: "北京"
            }
        },
        // $on 绑定自定义事件
        mounted(){
            this.$bus.$on('hello', (data)=>{
                console.log('我是School组件，我收到了数据',data)
            })
        },
        // $off 解绑自定义事件
        beforeDestroy(){
            this.$bus.$off('hello')
        }
    }
</script>

<style>
    .demo{
        background-color: yellow;
    }
</style>