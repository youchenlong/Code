"""数据库操作"""

from models.test import testtb, db

class testop():
    def __init__(self):
        self.__fields__ = ['id', 'name', 'sex', 'phone', 'email']
    
    def insertUserRecord(self, id, name, sex, phone, email):
        item = testtb(id=id, name=name, sex=sex, phone=phone, email=email)
        db.session.add(item)
        db.session.commit()
    
    def deleteUserRecord(self, id):
        item = testtb.query.filter(id).first()
        db.session.delete(item)
        db.session.commit()

    def updateUserPhone(self, id, phone):
        item = testtb.query.filter(testtb.id == id).first()
        # item.update({"phone": phone})
        item.phone = phone
        db.session.commit()

    def findUserRecord(self, id):
        return testtb.query.filter(testtb.id == id).first()