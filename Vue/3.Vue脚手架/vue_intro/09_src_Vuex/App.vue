<template>
    <!--
        Vuex 实现数据共享
            Actions 响应动作
            Mutations 操作数据
            State 保存数据
            Getters 加工数据
    -->
    <div>
        <Count/>
    </div>
</template>

<script>
    import Count from './components/Count'
    export default {
        name: 'App',
        components: {
            Count
        },
        mounted(){
            console.log(this)
        }
    }
</script>