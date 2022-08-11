from db_config import db_init as db


# 公司创建列表
class companyCreate(db.Model):
    __tablename__ = 'companyCreate'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(30))
    HR = db.Column(db.String(30))

