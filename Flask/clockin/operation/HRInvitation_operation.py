from models.HRInvitation import HRInvitation, db


# 用户模块操作类
class HRInvitation_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['ID',
                           'employee',
                           'HR',
                           'companyName']

    # 操作写在下面
    def insertInvitationRecord(self, employee, HR, companyName):
        HRI = HRInvitation(employee=employee, HR=HR, companyName=companyName)
        db.session.add(HRI)
        db.session.commit()

