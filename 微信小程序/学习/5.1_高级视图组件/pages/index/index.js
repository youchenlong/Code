// index.js
// 获取应用实例
const app = getApp()

Page({
  data: {
    audioContext: '',
    videoContext: '',
    cameraContext: '',
  },
  // 事件处理函数
 onLoad: function() {
   this.audioContext = wx.createAudioContext('audio');
   this.videoContext = wx.createVideoContext('video');
   this.cameraContext = wx.createCameraContext();
 },
 playAudio: function() {
  this.audioContext.play();
 },
 pauseAudio: function() {
   this.audioContext.pause();
 },
 playVideo: function() {
   this.videoContext.play();
 },
 pauseVideo: function() {
   this.videoContext.pause();
 },
 takephoto: function() {
   this.cameraContext.takePhoto();
 },
 startrecord: function() {
  this.cameraContext.startRecord();
 },
 stoprecord: function() {
   this.cameraContext.stopRecord();
 }
})
