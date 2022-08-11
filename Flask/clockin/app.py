from flask import Flask

from db_config import app

# 解决跨域
from flask_cors import CORS

CORS(app, supports_credentias=True)

# 导入蓝图
from handler.identify import identify
from handler.infoFind import infoFind
from handler.company import company
from handler.faceID import faceID
from handler.employeeManage import employeeManage

app.register_blueprint(identify, url_prefix="/identify")
app.register_blueprint(infoFind, url_prefix='/infoFind')
app.register_blueprint(company, url_prefix='/company')
app.register_blueprint(faceID, url_prefix='/faceID')
app.register_blueprint(employeeManage, url_prefix='/employeeManage')


@app.route('/')
def welcome():
    return "智慧考勤系统"


# 启动web后台服务
# flask服务启动 设置ip 端口
if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
