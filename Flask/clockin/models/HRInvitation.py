from db_config import db_init as db


# 邀请新员工列表
class HRInvitation(db.Model):
    __tablename__ = 'HRInvitation'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee = db.Column(db.String(30))
    HR = db.Column(db.String(30))
    companyName = db.Column(db.String(30))



