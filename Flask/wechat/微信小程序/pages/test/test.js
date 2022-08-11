// pages/test/test.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    // 视频的url，初始时刻默认为空
    target_url: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    wx.request({
      url: 'http://localhost:5000/test/getUrl?p=1',
      method: 'GET',
      data: {},
      // 下面使用箭头函数，不能使用普通函数，否则setData不能使用
      success:(res) => {
        console.log(res)
        this.setData({
          target_url: res.data._url
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})