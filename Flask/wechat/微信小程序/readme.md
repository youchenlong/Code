# 乡村普法小程序

## 程序结构
- app.js 小程序入口文件
- app.json 小程序全局配置
  - pages 页面路径列表
  - tabBar 导航栏
- app.wxss 小程序公共样式
- pages 页面
  - xxx
    - xxx.wxml 页面文件
      - 插值语法 ```{{}}```
      - 条件渲染 ```wx:if```
      - 列表渲染 ```wx:for```
      - 常用组件
        - view组件
          * view
          * scroll-view
          * swipper
          * movable-view
        - 基础视图组件
          * icon
          * text
          * progress
          * button
        - 用户输入组件
          * checkbox
          * radio
          * input
          * switch
          * label
          * slider
          * textarea
        - 选择器组件
          * selector
          * multiSelector
          * date
          * time
          * region
        - 高级视图组件
          * navigator
          * image
          * audio
          * video
          * camera
          * map
    - xxx.wxss 样式
      - 文档流
        - 块元素 
          * div 
          * p 
          * h1-h6 
          * br 
          * ol 
          * ul
        - 行内元素 
          * a 
          * input 
          * span 
          * select 
          * img
      - 盒子模型
        - content 内容区
        - padding 内边距
        - border  边框
        - margin  外边距 
      - 浮动
        - 水平布局，文字环绕
      - 定位
        - static 默认值
        - relative 相对定位
        - absolute 绝对定位
        - fixed 固定定位
        - sticky 粘滞定位
      - 常用居中方式
        - 水平居中
          ```width: 100px; margin: 0 auto;```
          ```text-align:center;```
          ```display：inline-block;text-align:center;```
        - 垂直居中
          ```height: 100px; line-height: 100px;```
    - xxx.js 脚本
      - 数据绑定 ```data```
      - 事件处理
      - 生命周期函数
      - 网络请求 
        ```javascript
        wx.request
        ```
      - 缓存 
        ```javascript
        wx.setStorage
        wx.getStorage
        wx.removeStorage
        ```
      - 用户授权
        ```javascript
        wx.getUserProfile
        ```
      - 页面跳转
        ```
        wx.navigateTo
        wx.redirectTo
        wx.reLaunch
        wx.switchTab
        ```
    - xxx.json 配置信息

## 开发工具
- 微信开发者工具
