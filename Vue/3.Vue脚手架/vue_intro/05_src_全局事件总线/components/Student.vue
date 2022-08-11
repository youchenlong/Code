<template>
    <div class="demo">
        <h2>{{name}}</h2>
        <h2>{{age}}</h2>
        <button @click="sendStudentName">把学生名发给School组件</button>
    </div>
</template>

<script>
    export default {
        name: 'Student',
        data(){
            return{
                name: "张三",
                age: 18
            }
        },
        methods: {
            sendStudentName(){
                // $emit 触发自定义事件
                this.$bus.$emit('hello', this.name)
            }
        }
    }
</script>

<style>
    .demo{
        background-color: yellow;
    }
</style>