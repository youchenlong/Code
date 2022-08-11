from db_config import db_init as db


# 用户列表
class userList(db.Model):
    __tablename__ = 'userList'
    username = db.Column(db.String(30), primary_key=True, autoincrement=False)
    password = db.Column(db.String(30))
    name = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(30))
    position = db.Column(db.String(30))
    companyName = db.Column(db.String(30))


