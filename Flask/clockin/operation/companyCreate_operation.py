from models.companyCreate import companyCreate, db


# 用户模块操作类
class companyCreate_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['ID',
                           'companyName',
                           'HR']

    # 操作写在下面
    def createCompany(self, companyName, HR):
        cc = companyCreate(companyName=companyName, HR=HR)
        db.session.add(cc)
        db.session.commit()