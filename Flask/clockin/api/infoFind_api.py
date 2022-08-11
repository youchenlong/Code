from operation.userList_operation import userList_Operation
from operation.clockin_operation import clockin_Operation
from operation.companyCreate_operation import companyCreate_Operation
from operation.companyList_operation import companyList_Operation
from operation.employeeApplication_operation import employeeApplication_Operation
from operation.HRInvitation_operation import HRInvitation_Operation
from operation.employeeDelete_operation import employeeDelete_Operation
from utils.data_process import *
from api.employeeManage_api import employeeInfoFind


# 操作写下面
def mInfo(username):
    # 数据库查询--
    userList_p = userList_Operation()
    # 在userList中查找用户的个人信息，并返回
    result_data = userList_p.findUserRecord(username)
    result = Class_To_Data(result_data, userList_p.__fields__)
    return result


def aInfo(employee, date):
    result = employeeInfoFind(employee, date)
    return result
