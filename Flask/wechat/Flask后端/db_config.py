from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask应用实例
app = Flask(__name__)

# 数据库配置
# 协议 mysql+pymysql
# 用户名 root（用自己的用户名）
# 密码 root（用自己的密码）
# IP地址 localhost
# 端口 3306
# 数据库名 wechat
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/wechat"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db_init = SQLAlchemy(app)