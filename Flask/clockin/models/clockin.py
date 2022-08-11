from db_config import db_init as db


# 打卡列表
class clockin(db.Model):
    __tablename__ = 'clockin'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee = db.Column(db.String(30))
    date = db.Column(db.Date)



