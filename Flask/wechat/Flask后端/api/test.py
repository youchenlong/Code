"""业务逻辑"""

from operation.test import testop

def api_login(id):
    op = testop()
    user = op.findUserRecord(id)
    if not user:
        return {'code': -1, 'message': "user dosen't exist!"}
    return {'code': 0, 'message': "login success"}

def api_register(id, name, sex, phone, email):
    op = testop()
    if op.findUserRecord(id):
        return {'code': -1, 'message': "user already exists!"}
    op.insertUserRecord(id, name, sex, phone, email)
    return {'code': 0, 'message': "register success"}
