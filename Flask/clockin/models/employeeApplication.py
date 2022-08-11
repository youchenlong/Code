from db_config import db_init as db


# 员工申请列表
class employeeApplication(db.Model):
    __tablename__ = 'employeeApplication'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee = db.Column(db.String(30))
    HR = db.Column(db.String(30))
    companyName = db.Column(db.String(30))
    status = db.Column(db.Boolean)


