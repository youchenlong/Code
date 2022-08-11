"""对象关系映射"""

from db_config import db_init as db

class testtb(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.String(30), primary_key=True, autoincrement=False)
    name = db.Column(db.String(30))
    sex = db.Column(db.String(1))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(30))