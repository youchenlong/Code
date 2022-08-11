from operation.userList_operation import userList_Operation
from operation.clockin_operation import clockin_Operation
from operation.companyCreate_operation import companyCreate_Operation
from operation.companyList_operation import companyList_Operation
from operation.employeeApplication_operation import employeeApplication_Operation
from operation.HRInvitation_operation import HRInvitation_Operation
from operation.employeeDelete_operation import employeeDelete_Operation
from utils.data_process import *


# 操作写下面
def lgin(username, password):
    # 数据库查询--
    userList_p = userList_Operation()
    # 判断用户名和密码是否正确，如果用户名和密码正确，返回“登录成功”，否则返回“登录失败”
    user = userList_p.findUserRecord(username).first()
    # 如果用户不存在，返回“用户不存在”
    if not user:
        return {'code': 1, 'message': "user dosen't exist"}
    if password == user.password:
        return {'code': 0, 'message': "success", "position": user.position}
    return {'code': 2, 'message': "failed"}


def reg(username, password, name, phone, email):
    # 数据库查询--
    userList_p = userList_Operation()
    # 1、用户名是否重复，如果重复，返回“用户名已存在”，如果不存在，进行下一步
    if userList_p.findUserRecord(username).first():
        return {'code': -1, 'message': "username duplicate"}
    # 2、向userList表中插入一条记录，并返回”注册成功“
    userList_p.insertUserRecord(username, password, name, phone, email)
    return {'code': 0, 'message': "success"}
