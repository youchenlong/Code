<template>
  <div>
      <!-- <h1>当前求和结果为：{{$store.state.sum}}</h1>
      <h3>放大十倍后的结果为：{{$store.getters.bigSum}}</h3> -->
      <h1>当前求和结果为：{{sum}}</h1>
      <h3>放大十倍后的结果为：{{bigSum}}</h3>
      <select v-model.number="n">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
      </select>
      <button @click="add(n)">+</button>
      <button @click="sub(n)">-</button>
      <button @click="addOdd(n)">当前求和为奇数时再加</button>
      <button @click="addWait(n)">等一等再加</button>
  </div>
</template>

<script>
    import {mapState, mapGetters, mapMutations, mapActions} from 'vuex'
    export default {
        name: 'Count',
        data(){
            return {
                n: 1
            }
        },
        computed: {
            ...mapState(['sum']),
            ...mapGetters(['bigSum'])
        },
        methods: {
            // add(n){
            //     this.$store.commit('add', n)
            // },
            // sub(n){
            //     this.$store.commit('sub', n)
            // },
            // addOdd(n){
            //     this.$store.dispatch('addOdd', n)
            // },
            // addWait(n){
            //     this.$store.dispatch('addWait', n)
            // },

            ...mapMutations(['add', 'sub']),
            ...mapActions(['addOdd', 'addWait'])
        }
    }
</script>

<style>
    *{
        margin-left: 5px;
    }
</style>