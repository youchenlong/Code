import datetime

from sqlalchemy import and_

from models.clockin import clockin, db


# 用户模块操作类
class clockin_Operation():
    def __init__(self):
        self.__fields__ = ['ID',
                           'employee',
                           'date']

    # 操作写在下面
    def inserAttendRecord(self, employee, date):
        c = clockin(employee=employee, date=date)
        db.session.add(c)
        db.session.commit()

    def findAttendRecord(self, employee, date):
        return clockin.query.filter(clockin.employee == employee, clockin.date == date)
