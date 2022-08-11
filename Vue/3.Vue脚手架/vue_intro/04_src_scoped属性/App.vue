<template>
    <!--
        scoped: 让样式在局部生效，避免冲突
    -->
    <div>
        <School></School>
        <Student></Student>
    </div>
</template>

<script>

    /*引入组件*/
    import School from './components/School.vue'
    import Student from './components/Student.vue'

    export default {
        name: 'App',
        /*注册组件*/
        components: {
            School,
            Student
        }
    }
</script>

<style>

</style>