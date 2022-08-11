<template>
    <!--
        $bus 全局事件总线
        $on 绑定自定义事件
        $off 解绑自定义事件
        $emit 触发自定义事件
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