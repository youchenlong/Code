import json

from flask import Blueprint, request, Response, jsonify
from api.company_api import *

company = Blueprint('company', __name__)


@company.route('/companyCreate', methods=['POST'])
def companyCreate():
    # 获取输入的公司名和HR
    data = json.loads(request.data)
    companyName = data.get("companyName")
    HR = data.get("HR")
    # companyName = 'companyA'
    # HR = '20181736'
    result = cCreate(companyName, HR)
    return jsonify(result)


@company.route('/employeeApplication', methods=['POST'])
def employeeApplication():
    # 获取申请人和审批人和公司名
    data = json.loads(request.data)
    employee = data.get("employee")
    HR= data.get("HR")
    companyName = data.get("companyName")
    # employee = '20181745'
    # HR = '20181736'
    # companyName = 'companyA'
    result = eApplication(employee, HR, companyName)
    return jsonify(result)
