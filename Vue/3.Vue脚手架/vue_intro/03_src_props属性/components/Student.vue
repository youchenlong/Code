<template>
    <div>
        <h2>{{name}}</h2>
        <h2>{{sex}}</h2>
        <h2>{{age-14}}</h2>
    </div>
</template>

<script>
    export default {
        name: 'Student',
        data(){
            return{

            }
        },
        props: ['name', 'sex', 'age']
        // props: {
        //     name: String,
        //     age: Number, 
        //     sex: String
        // }
        // props: {
        //     name: {
        //         type: String,
        //         required: true
        //     },
        //     age: {
        //         type: Number,
        //         default: 18
        //     },
        //     sex: {
        //         type: String,
        //         required: true
        //     }
        // }
    }
</script>

<style>

</style>