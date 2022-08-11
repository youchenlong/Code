<template>
  <ul class="todo-main">
    <transition-group
      name="animate__animated animate__bounce"
      appear
      enter-active-class="animate__backInRight"
      leave-active-class="animate__backOutRight"
    >
      <MyItem 
        v-for="todoObj in todos" 
        :key="todoObj.id" 
        :todo="todoObj" 
      />
    </transition-group>
  </ul>
</template>

<script>
    import 'animate.css'
    import MyItem from "./MyItem"

    export default {
        name: 'MyList',
        components: {
            MyItem
        },
        props: ['todos']
    }
</script>

<style scoped>
/*main*/
.todo-main {
  width: 560px;
  margin-left: 0px;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0px;
}
/* .todo-empty {
  height: 40px;
  line-height: 40px;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding-left: 5px;
  margin-top: 10px;
} */
</style>