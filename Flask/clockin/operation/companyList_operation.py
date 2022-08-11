from models.companyList import companyList, db


# 用户模块操作类
class companyList_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['companyID',
                           'companyName']

    # 操作写在下面
    def insertCompanyRecord(self, companyName):
        cl = companyList(companyName=companyName)
        db.session.add(cl)
        db.session.commit()

    def findCompanyRecord(self, companyName):
        return companyList.query.filter(companyList.companyName == companyName)
