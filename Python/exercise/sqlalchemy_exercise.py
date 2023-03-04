from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:root@localhost:3306/wechat")
Session = sessionmaker(bind=engine)
session = Session()

class testtb(Base):
    __tablename__ = 'test_transformer'
    id = Column(String(30), primary_key=True, autoincrement=False)
    name = Column(String(30))
    sex = Column(String(1))
    phone = Column(String(30))
    email = Column(String(30))

Base.metadata.create_all(engine)

def insertRecord(id, name, sex, phone, email):
    item = testtb(id, name, sex, phone, email)
    session.add(item)
    session.commit()

def deleteRecord(name):
    item = session.query(testtb).filter(testtb.name==name).first()
    session.delete(item)
    session.commit()

def updateRecord(name, phone):
    item = session.query(testtb).filter(testtb.name==name).first()
    item.phone = phone
    session.commit()

def findRecord(name):
    item = session.query(testtb).filter(testtb.name==name).first()
    return item

# insertRecord(id='2018xxxx', name='xiaoming', sex='男', phone='173xxxxxxxx', email='xxxxxxxxxx@qq.com')
# deleteRecord(name="xiaoming")
# updateRecord(name="xiaoming", phone="130xxxxxxxx")
# findRecord(name="xiaoming")


