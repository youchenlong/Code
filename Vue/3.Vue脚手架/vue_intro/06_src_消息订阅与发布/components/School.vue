<template>
    <div class="demo">
        <h2>{{name}}</h2>
        <h2>{{address}}</h2>
    </div>
</template>

<script>
    import pubsub from 'pubsub-js'

    export default {
        name: 'School',
        data(){
            return{
                name: "尚硅谷",
                address: "北京"
            }
        },
        methods: {
            demo(msgName, data){
                console.log('有人发布了hello消息', msgName, data)
            }
        },
        mounted(){
            this.pubId = pubsub.subscribe('hello', this.demo)
        },
        beforeDestroy(){
            pubsub.unsubscribe(this.pubId)
        }
    }
</script>

<style>
    .demo{
        background-color: yellow;
    }
</style>