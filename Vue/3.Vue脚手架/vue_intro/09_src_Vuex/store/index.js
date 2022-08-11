import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 响应动作
const actions = {
    // add(context, value){
    //     context.commit('add', value)
    // },
    // sub(context, value){
    //     context.commit('sub', value)
    // },
    addOdd(context, value){
        if(context.state.sum % 2){
            context.commit('add', value)
        }
    },
    addWait(context, value){
        setTimeout(()=>{
            context.commit('add', value)
        }, 500)
    }
}
// 操作数据
const mutations = {
    add(state, value){
        state.sum += value
    },
    sub(state, value){
        state.sum -= value
    }
}
// 存储数据
const state = {
    sum: 0
}
// 加工数据
const getters = {
    bigSum(state){
        return state.sum * 10
    }
}

export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters
})