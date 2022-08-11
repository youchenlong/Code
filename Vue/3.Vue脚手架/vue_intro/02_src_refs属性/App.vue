<template>
    <div>
        <!--
            ref: 给 元素 和 子组件 注册引用信息
        -->
        <h1 v-text="msg" ref="title"></h1>
        <School ref="sch"></School>
        <button @click="showDOM">点我获取DOM</button>
    </div>
</template>

<script>

    import School from './components/School.vue'

    export default {
        name: 'App',
        components: {
            School
        },
        data(){
            return {
                msg: "欢迎学习Vue"
            }
        },
        methods: {
            showDOM(){
                console.log(this.$refs.title)
                console.log(this.$refs.sch)
            }
        }
    }
</script>