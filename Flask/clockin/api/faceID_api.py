from operation.userList_operation import userList_Operation
from operation.clockin_operation import clockin_Operation
from operation.companyCreate_operation import companyCreate_Operation
from operation.companyList_operation import companyList_Operation
from operation.employeeApplication_operation import employeeApplication_Operation
from operation.HRInvitation_operation import HRInvitation_Operation
from operation.employeeDelete_operation import employeeDelete_Operation
from utils.data_process import *


# 操作写下面
def fInfoInput(username, password):
    # 数据库查询--
    userList_p = userList_Operation()
    # 判断用户名和密码是否正确，如果用户名和密码正确，返回“登录成功”，否则返回“登录失败”
    user = userList_p.findUserRecord(username).first()
    # 如果用户不存在，返回“用户不存在”
    if not user:
        return {'code': 1, 'message': "user dosen't exist"}
    if password == user.password:
        return {'code': 0, 'message': "success"}
    return {'code': 2, 'message': "failed"}


def cin(username, date):
    # 查询数据库--
    clockin_p = clockin_Operation()
    # 如果当天已经打过卡，返回“您今日已完成打卡”，否则进行下一步
    result_data = clockin_p.findAttendRecord(username, date).all()
    if result_data:
        return {'code': -1, 'message': 'you have already clockin today!'}
    # 在clockin中插入一条记录
    clockin_p.inserAttendRecord(username, date)
    # 返回“打卡成功”
    return {'code': 0, 'message': 'success'}

