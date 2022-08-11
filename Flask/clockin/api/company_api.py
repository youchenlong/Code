from operation.userList_operation import userList_Operation
from operation.clockin_operation import clockin_Operation
from operation.companyCreate_operation import companyCreate_Operation
from operation.companyList_operation import companyList_Operation
from operation.employeeApplication_operation import employeeApplication_Operation
from operation.HRInvitation_operation import HRInvitation_Operation
from operation.employeeDelete_operation import employeeDelete_Operation
from utils.data_process import *
from utils.sql import *


# 操作写下面
def cCreate(companyName, HR):
    # 数据库查询--
    userList_p = userList_Operation()
    companyList_p = companyList_Operation()
    companyCreate_p = companyCreate_Operation()
    # 1、如果HR没有注册，返回“您未注册”，如果已注册，进行下一步
    if not userList_p.findUserRecord(HR).first():
        return {'code': 4, 'message': "you have not register!"}
    # 2、外部数据库中是否存在该公司，如果不存在，返回”您要创建的公司不存在“，如果存在，进行下一步
    res = SQLHelper.fetch_one("select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA= %s and TABLE_NAME= %s", ['externalcompany', companyName])
    if not res:
        return {'code': 1, 'message': "company doesn't exsit!"}
    _companyName = res['TABLE_NAME']
    # 3、HR是否为公司的HR，如果不是公司的HR，返回”您不是公司的HR，无法创建公司“，如果是公司的HR，进行下一步
    result_data = SQLHelper.fetch_one("select * from %s where username = %s" % (_companyName, HR), [])
    if result_data['position'] != 'HR':
        return {'code': 2, 'message': "you are not HR of the company!"}
    # 4、在companyList表中查询公司是否重复，如果重复，返回”您要创建的公司已存在“，如果不重复，进行下一步
    if companyList_p.findCompanyRecord(companyName).first():
        return {'code': 3, 'message': "company duplicate!"}
    # 5、在companyCreate表中插入一条记录，并在companyList列表中插入一条记录，返回”创建公司成功“
    companyList_p.insertCompanyRecord(companyName)
    companyCreate_p.createCompany(companyName, HR)
    # 6、修改HR为的职务为HR，公司为指定的公司
    userList_p.updateUserCompany(HR, companyName)
    userList_p.updateUserPosition(HR, "HR")
    return {'code': 0, 'message': 'success'}


def eApplication(employee, HR, companyName):
    # 数据库查询--
    userList_p = userList_Operation()
    companyList_p = companyList_Operation()
    employeeApplication_p = employeeApplication_Operation()
    # 1、公司是否存在，如果不存在，返回“公司不存在”，如果存在，进行下一步
    if not companyList_p.findCompanyRecord(companyName).first():
        return {'code': 1, 'message': "company doesn't exsit!"}
    # 2、申请人是否是公司的员工，如果在，返回“您已是公司的员工”，如果不在，进行下一步
    if userList_p.findUserRecord(employee).first().companyName == companyName:
        return {'code': 2, 'message': "you are already employee of the company!"}
    # 3、审批人是否在公司的员工列表中，如果不在，返回“审批人不在公司的列表中”，如果在，进行下一步
    result_data = userList_p.findUserRecord(HR).first()
    if result_data.companyName != companyName:
        return {'code': 3, 'message': "approver is not in the company!"}
    # 4、审批人是否是公司的HR，如果不是，返回“审批人不是公司的HR”，如果是，进行下一步
    if result_data.position != 'HR':
        return {'code': 4, 'message': "approver is not HR of the company!"}
    # 5、申请人是否有相同的申请在等待审批，如果有，返回“审批已经存在”，如果没有，进行下一步
    if employeeApplication_p.findApplicationRecord(employee, HR, companyName).first():
        return {'code': 5, 'message': "application is existed!"}
    # 6、、在employeeApplication添加日志信息，返回“等待HR审批“
    employeeApplication_p.insertApplicationRecord(employee, HR, companyName)
    return {'code': 0, 'message': 'success'}
