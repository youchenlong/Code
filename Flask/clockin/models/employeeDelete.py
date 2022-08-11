from db_config import db_init as db


# 员工删除列表
class employeeDelete(db.Model):
    __tablename__ = 'employeeDelete'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    HR = db.Column(db.String(30))
    employee = db.Column(db.String(30))
    companyName = db.Column(db.String(30))



