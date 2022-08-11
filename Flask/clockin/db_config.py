from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)

SQLALCHEMY_BINDS = {
    'externalcompany': "mysql+pymysql://root:root@127.0.0.1:3306/externalcompany"
}

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/clockin"
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_init = SQLAlchemy(app)
