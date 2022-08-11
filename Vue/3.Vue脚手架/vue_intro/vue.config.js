module.exports = {
    // 关闭语法检查
    lintOnSave: false,
    // 配置代理
    devServer: {
        proxy: 'http://localhost:5000'
    }
}