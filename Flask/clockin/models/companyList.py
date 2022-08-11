from db_config import db_init as db


# 公司列表
class companyList(db.Model):
    __tablename__ = 'companyList'
    companyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(30))
