// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
   data: ["男", "女", "未知"],
   index: 0,
   address: [["省份1", "省份2"], ["城市1", "城市2"]],
   currentAddress: [0, 0],
   time: "16:06",
   date: "2021-3-28",
   region: ["四川省", "达州市", "大竹县"],
  },
  // 事件处理函数
  change: function(event) {
    this.setData({index:event.detail.value});
  },
  changeAddress: function(event) {
    this.setData({currentAddress:event.detail.value});
  },
  changeTime: function(event) {
    this.setData({time: event.detail.value});
  },
  changeDate: function(event) {
    this.setData({date: event.detail.value});
  },
  changeRegion: function(event) {
    this.setData({region: event.detail.value});
  }
})
