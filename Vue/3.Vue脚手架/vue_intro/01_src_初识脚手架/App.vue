<template>
    <div>
        <img src="./assets/logo.png" alt="logo">
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