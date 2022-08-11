// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    
  },
  // 事件处理函数
  getRequest:function(){
    wx.request({
      url: 'http://localhost:5000/test/getJson',
      method: 'GET',
      data: {},
      success : (res) => {
        console.log("数据请求成功", res.data)
      },
      fail: (res) => {
        console.log("数据请求失败", res)
      }
    })
  }
})
