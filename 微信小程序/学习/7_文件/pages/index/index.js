// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    
  },
  // 事件处理函数
  downloadFile: function(){
    wx.downloadFile({
      url: 'https://pic3.zhimg.com/v2-58d652598269710fa67ec8d1c88d8f03_r.jpg?source=1940ef5cp',
      success: (res) => {
        console.log("文件下载成功")
        wx.setStorage({
          key: 'tempFilePath',
          data: res.tempFilePath
        })
      },
      fail: (res) => {
        console.log("文件下载失败")
      }
    })
  },
  uploadFile: function(){
    wx.getStorage({
      key: "tempFilePath",
      success: (res) => {
        const tempFilePath = res.data
        wx.uploadFile({
          filePath: tempFilePath,
          name: '上传文件',
          url: 'http://localhost:5000/',
          success: (res) => {
            console.log("文件上传成功", res.data)
          },
          fail: (res) => {
            console.log("文件上传失败")
          }
        })
      }
    })
  }
})
