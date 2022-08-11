import json

from flask import Blueprint, request, Response, jsonify
from api.employeeManage_api import *

employeeManage = Blueprint('employeeManage', __name__)


@employeeManage.route('/employeeList', methods=['POST'])
def employeeList():
    data = json.loads(request.data)
    companyName = data.get("companyName")
    result_list = employeeListShow(companyName)
    return jsonify(result_list)


@employeeManage.route("/employeeInfo", methods=['POST'])
def employeeInfo():
    data = json.loads(request.data)
    username = data.get("username")
    if data.get("date"):
        date = datetime.datetime.strptime(data.get("date"), '%Y-%m-%d').date()
    else:
        date = datetime.datetime.now().date()
    result_user = employeeInfoFind(username, date)
    return jsonify(result_user)


@employeeManage.route("/approval", methods=['POST'])
def Approval():
    data = json.loads(request.data)
    mode = data.get("mode")
    employee = data.get("employee")
    HR = data.get("HR")
    if mode == 0:
        result_data = jsonify(getApplicationList(HR))
    elif mode == 1:
        result_data = HRApproval_1(employee, HR)
    elif mode == 2:
        result_data = HRApproval_2(employee, HR)
    return result_data


@employeeManage.route("/position", methods=['POST'])
def Position():
    data = json.loads(request.data)
    employee = data.get("employee")
    position = data.get("position")
    result_data = positionManage(employee, position)
    return result_data


@employeeManage.route("/invitation", methods=['POST'])
def Invitation():
    data = json.loads(request.data)
    employee = data.get("employee")
    HR = data.get("HR")
    result_data = HRInvitation(employee, HR)
    return result_data


@employeeManage.route("/delete", methods=['POST'])
def Delete():
    data = json.loads(request.data)
    HR = data.get("HR")
    employee = data.get("employee")
    result_data = employeeDelete(HR, employee)
    return result_data
