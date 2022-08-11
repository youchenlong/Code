from models.userList import userList, db


# 用户模块操作类
class userList_Operation():
    # 应该映射到user表的字段
    def __init__(self):
        self.__fields__ = ['username',
                           'password',
                           'name',
                           'phone',
                           'email',
                           'position',
                           'companyName'
                           ]

    # 操作写在下面
    def insertUserRecord(self, username, password, name, phone, email):
        user = userList(username=username, password=password, name=name,
                        phone=phone, email=email)
        db.session.add(user)
        db.session.commit()

    def updateUserPosition(self, username, position):
        userList.query.filter(userList.username == username).update({"position": position})
        db.session.commit()
        return userList.query.filter(userList.username == username, userList.position == position)

    def updateUserCompany(self, username, companyName):
        userList.query.filter(userList.username == username).update({"companyName": companyName})
        db.session.commit()

    def findUserRecord(self, username):
        return userList.query.filter(userList.username == username)

    def findAllEmployee(self, companyName):
        return userList.query.filter(userList.companyName == companyName).all()

    # 以下为额外功能
    def deleteUserCompany(self, username):
        userList.query.filter(userList.username == username).update({"companyName": None, "position": None})
        db.session.commit()
