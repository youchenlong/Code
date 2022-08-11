<template>
    <!--
        消息订阅与发布 需要引入第三方库(例如pubsub-js)
        publish
        subscribe
    -->
    <div>
        <School></School>
        <Student></Student>
    </div>
</template>

<script>

    import School from './components/School.vue'
    import Student from './components/Student.vue'

    export default {
        name: 'App',
        components: {
            School,
            Student
        }
    }
</script>

<style>

</style>