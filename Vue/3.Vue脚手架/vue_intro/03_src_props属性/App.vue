<template>
    <!--3.使用组件-->
    <div>
        <!--
            props: 父组件与子组件之间通信
            默认类型为String
            只读类型
        -->
        <Student name="老王" sex="男" :age="40"></Student>
    </div>
</template>

<script>

    /*1.引入组件*/
    import Student from "./components/Student.vue"

    export default {
        name: 'App',
        /*2.注册组件*/
        components: {
            Student
        },
        data(){
            return {

            }
        },
        methods: {

        }
    }
</script>