1.开发工具
注册小程序开发账号（https://mp.weixin.qq.com/）
微信开发者工具(https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)
    功能（左上角）--模拟器、编辑器、调试器


2.目录结构
project.config.json（尽量别改）
    工程配置文件
app.js（尽量别改）
    小程序入口文件
app.json（尽量别改）
    小程序全局配置
    pages--页面路径列表
pages
    indexs--存放页面文件
        .wxml   页面文件（定义了各种组件，view组件（view，scroll-view, swipper, movable-view），
                                        基础视图组件（icon, text, progress, button）,
                                        用户输入组件（checkbox, radio, input, switch, label, slider, textarea）
                                        选择器组件（selector, multiSelector, date, time, region）,
                                        高级视图组件（navigator, image, audio, video, camera, map））
        .css    样式（选择器+属性）
                选择器--元素选择器、类选择器、id选择器
        .js     脚本(默认使用javascript
                    网络请求--wx.request
                    文件--wx.downloadFile, wx.uploadFile, wx.saveFile, wx.removeSavedFile, wx.openDocument
                    文件管理器--wx.getFileSystemManager
                    缓存--wx.setStorage, wx.getStorage, wx.removeStorage
                    系统弹窗--消息框wx.showToast, 对话框wx.showModal, 等待框wx.showLoading
                    系统信息与更新--wx.getSystemInfo
                    获取用户信息--wx.authorize, wx.getUserInfo
                    功能插件--微信支付wx.requestPayment, 用户运动数据wx.getWeRunData
                    获取设备功能接口--Wifi, 电话与联系人， 屏幕方向与亮度， 电量， 振动与扫码)
        .json   配置信息（无需修改）
    logs--日志信息（无需修改）
utils（无需修改）

