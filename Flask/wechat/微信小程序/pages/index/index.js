// pages/index/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    recommend: [{
      'title': '法学专业导论',
      'image': 'https://boot-img.xuexi.cn/image/1005/process/636f9581beca4d018627a3b19f8b051a.jpg',
    },{
      'title': '经济生活中的法律',
      'image': 'https://boot-img.xuexi.cn/image/1005/process/10abd9ad085c43f5ab406daf2e6806d9.jpg',
    },{
      'title': '消费者保护法',
      'image': 'https://boot-img.xuexi.cn/image/1005/process/186c6167785147609eb0698326e4daed.jpg',
    }],
    show:false,//控制下拉列表的显示隐藏，false隐藏、true显示
    selectData:['搜标题','搜作者','搜类别'],//下拉列表的数据
    index:0,//选择的下拉列表下标
    nav1_selected: 0,//一级菜单栏
    nav2_selected: 0,//二级菜单栏
    index1:0,
    index2:0,
    nav1_list: ['看视频', '读条文'],
    footer_message: '如有问题，请与我联系，联系方式：xxxxxxxx',
    search_data:[],
    return_data:[],
    ztoView: '',
    zlist_video: ["热门", "劳动纠纷", "农业", "林业","类型1", "类型2", "类型3", "类型4"],
    zlist_article:["热门","农业"]
  },

    // 点击下拉显示框
  selectTap(){
    this.setData({
     show: !this.data.show
    });
  },
    // 点击下拉列表
  optionTap(e){
    let Index=e.currentTarget.dataset.index;//获取点击的下拉列表的下标
    console.log(Index)
    this.setData({
     index1:Index,
     show:!this.data.show
    });
  },
  //一级菜单栏切换
  nav1_selected: function (e) {
    console.log(e)
    let that = this
    let index = e.currentTarget.dataset.index
    console.log(index)
    if (index == 0) {
      that.setData({
        nav1_selected: 0,
      })
    } else {
      that.setData({
        nav1_selected: 1,
      })
    }
  },
  bindchange(e) {
    let index = e.detail.current;
    this.setData({
        nav1_selected:index
    })
  },
  //二级菜单栏
  nav2_selected: function (e) {
    console.log(this.nav2_selected)
    let that = this
    let index = e.currentTarget.dataset.index
    if (index == 0) {
      that.setData({
        nav2_selected: 0,
      })
    }else if(index==1){
        that.setData({nav2_selected:1})
    }else if(index==2){
        that.setData({nav2_selected:2})
    }else if(index==3){
        that.setData({nav2_selected:3})
    }else if(index==4){
        that.setData({nav2_selected:4})
    }else if(index==5){
        that.setData({nav2_selected:5})
    }else if(index==6){
        that.setData({nav2_selected:6})
    } else {
      that.setData({
        nav2_selected: 7,
      })
    }
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