from models.employeeDelete import employeeDelete, db


# 用户模块操作类
class employeeDelete_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['ID',
                           'HR',
                           'employee',
                           'companyName']

    # 操作写在下面
    def insertDeleteRecord(self, HR, employee, companyName):
        ed = employeeDelete(HR=HR, employee=employee, companyName=companyName)
        db.session.add(ed)
        db.session.commit()

