// pages/login/login.js
Page({

  data: {
    userInfo: {}
  },

  onLoad: function (options) {
    // 再次登录--直接从本地存储读取用户信息
    this.setData({
      userInfo: wx.getStorageSync('userInfo')
    })
    if(this.data.userInfo){
      wx.switchTab({
        url: '/pages/index/index'
      })
    }
  },

  // 初次登陆--需要用户授权
  getUserProfile(e){
    console.log("getUserProfile")
    wx.getUserProfile({
      desc: '用户授权登录',
      success: (res) => {
        // 1.保存到本地存储
        wx.setStorageSync('userInfo', res.userInfo)
        // 2.跳转到主页
        this.setData({
          userInfo: res.userInfo,
        })
        setTimeout(function(){
          wx.switchTab({
            url: '/pages/index/index'
          })
        }, 1000)
      },
      fail: (res) => {
        console.log(res.errMsg)
      }
    })
  }
})