from typing import List
from operation.userList_operation import userList_Operation
from operation.clockin_operation import clockin_Operation
from operation.companyCreate_operation import companyCreate_Operation
from operation.companyList_operation import companyList_Operation
from operation.employeeApplication_operation import employeeApplication_Operation
from operation.HRInvitation_operation import HRInvitation_Operation
from operation.employeeDelete_operation import employeeDelete_Operation
from utils.data_process import *
import datetime


# 预备操作
def m_days(date):
    year = date.year
    month = date.month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        if year % 400 == 0:
            days = 29
        else:
            if year % 100 != 0 and year % 4 == 0:
                days = 29
            else:
                days = 28
    return days


# 操作写下面
def employeeListShow(companyName):
    userList_p = userList_Operation()
    result_data = userList_p.findAllEmployee(companyName)
    result_list = Class_To_Data(result_data, userList_p.__fields__)
    return result_list


def employeeInfoFind(username, today):
    clockin_p = clockin_Operation()
    days = m_days(today)
    date = datetime.date(today.year, today.month, 1)
    result = []
    for e in range(days):
        result.append(0)
    for e in range(days):
        if clockin_p.findAttendRecord(username, date).first():
            result[e] = 1
        date = date + datetime.timedelta(days=1)
    return result


def HRApproval_1(employee, HR):
    userList_p = userList_Operation()
    employeeApplication_p = employeeApplication_Operation()
    if userList_p.findUserRecord(employee).first():
        emp = Class_To_Data(userList_p.findUserRecord(employee).first(), userList_p.__fields__, 1)
        hr = Class_To_Data(userList_p.findUserRecord(HR).first(), userList_p.__fields__, 1)
        if emp.get("companyName"):
            result = {
                "code": -1,
                "message": "employee has been in one company"
            }
        else:
            userList_p.updateUserPosition(employee, '员工')
            userList_p.updateUserCompany(employee, hr.get("companyName"))
            employeeApplication_p.updateApplacationRecord(employee, HR, hr.get("companyName"))
            result = {
                "code": 0,
                "message": "apply success"
            }
    else:
        result = {
            "code": -1,
            "message": "no this employee"
        }
    return result


def HRApproval_2(employee, HR):
    userList_p = userList_Operation()
    employeeApplication_p = employeeApplication_Operation()
    hr = Class_To_Data(userList_p.findUserRecord(HR).first(), userList_p.__fields__, 1)
    employeeApplication_p.updateApplacationRecord(employee, HR, hr.get("companyName"))
    result = {
        "code": 0,
        "message": "refused application success"
    }
    return result


def getApplicationList(HR):
    userList_p = userList_Operation()
    employeeApplication_p = employeeApplication_Operation()
    hr = Class_To_Data(userList_p.findUserRecord(HR).first(), userList_p.__fields__, 1)
    result_data = employeeApplication_p.findApplicationList(HR, hr.get("companyName")).all()
    result_list = Class_To_Data(result_data, employeeApplication_p.__fields__)
    return result_list


def positionManage(username, position):
    userList_p = userList_Operation()
    if userList_p.updateUserPosition(username, position).first():
        result = {"code": 0, "message": "success"}
    else:
        result = {"code": -1, "message": "default"}
    return result


def HRInvitation(employee, HR):
    HRInvitation_p = HRInvitation_Operation()
    userList_p = userList_Operation()
    if not userList_p.findUserRecord(employee).first():
        result = {
            "code": -1,
            "message": "username not found"
        }
        return result
    if userList_p.findUserRecord(HR).first():
        emp = Class_To_Data(userList_p.findUserRecord(employee).first(), userList_p.__fields__, 1)
        hr = Class_To_Data(userList_p.findUserRecord(HR).first(), userList_p.__fields__, 1)
        if emp.get("companyName"):
            result = {
                "code": -1,
                "message": "employee has been in one company"
            }
        else:
            userList_p.updateUserPosition(employee, '员工')
            userList_p.updateUserCompany(employee, hr.get("companyName"))
            HRInvitation_p.insertInvitationRecord(employee, HR, hr.get("companyName"))
            result = {
                "code": 0,
                "message": "invitation success"
            }
    else:
        result = {
            "code": -1,
            "message": "no this employee"
        }
    return result


def employeeDelete(HR, employee):
    userList_p = userList_Operation()
    employeeDelete_p = employeeDelete_Operation()
    hr = Class_To_Data(userList_p.findUserRecord(HR).first(), userList_p.__fields__, 1)
    emp = Class_To_Data(userList_p.findUserRecord(employee).first(), userList_p.__fields__, 1)
    if hr.get("username") == emp.get("username"):
        result = {
            "code": -3,
            "message": "you cannot delete yourself!"
        }
        return result
    if hr.get("companyName") == emp.get("companyName"):
        userList_p.deleteUserCompany(employee)
        emp = Class_To_Data(userList_p.findUserRecord(employee).first(), userList_p.__fields__, 1)
        if not emp.get("companyName"):
            employeeDelete_p.insertDeleteRecord(HR, employee, hr.get("companyName"))
            result = {
                "code": 0,
                "message": "delete success"
            }
        else:
            result = {
                "code": -1,
                "message": "delete default"
            }
    else:
        result = {
                "code": -2,
                "message": "error: not the same company"
            }
    return result

