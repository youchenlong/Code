from models.employeeApplication import employeeApplication, db


# 用户模块操作类
class employeeApplication_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['ID',
                           'employee',
                           'HR',
                           'companyName',
                           'status']

    # 操作写在下面
    def insertApplicationRecord(self, employee, HR, companyName, status=False):
        ea = employeeApplication(employee=employee, HR=HR, companyName=companyName, status=status)
        db.session.add(ea)
        db.session.commit()

    def updateApplacationRecord(self, employee, HR, companyName):
        employeeApplication.query.filter(employeeApplication.employee==employee, employeeApplication.HR==HR, 
        employeeApplication.companyName==companyName, employeeApplication.status==False).update({"status":True})
        db.session.commit()

    def findApplicationRecord(self, employee, HR, companyName):
        return employeeApplication.query.filter(employeeApplication.employee==employee, 
        employeeApplication.HR==HR, employeeApplication.companyName==companyName, employeeApplication.status==False)

    def findApplicationList(self, HR, companyName):
        return employeeApplication.query.filter(employeeApplication.HR==HR, employeeApplication.companyName==companyName, 
        employeeApplication.status==False)
 