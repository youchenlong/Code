// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    
  },
  // 事件处理函数
  Grade:function(){
    var score = -100;
   var grade;
   if(score >= 90){
     grade = "优秀";
   }
   else if(score >= 70 && score < 90){
     grade = "良好";
   }
   else if(score >= 60 && score < 70){
     grade = "及格";
   }
   else if(score >= 0 && score < 60){
     grade = "不及格";
   }
   else{
     grade = "?";
   }
   console.log("你的考试成绩为：" + score);
   switch(grade){
     case "优秀":{
      console.log("太秀了");
     }
     break;
     case "良好":{
       console.log("哎哟，不错哦");
     }
     break;
     case "及格":{
       console.log("恭喜恭喜，及格了");
     }
     break;
     case "不及格":{
       console.log("不要灰心，下次一定");
     }
     break;
     default:{
       console.log("你考了个啥玩意呢？");
     }
   }
  },
  sum1to100:function(){
    var sum = 0;
    for(var i = 1; i <= 100; i++){
      sum += i;
    }
    console.log(sum);
  }
})
