import datetime
import json

from flask import Blueprint, request, Response, jsonify
from api.infoFind_api import *

infoFind = Blueprint('infoFind', __name__)


@infoFind.route('/myInfo', methods=['POST'])
def myInfo():
    # 获取用户名
    data = json.loads(request.data)
    username = data.get("username")
    # username = '20181736'
    result = mInfo(username)
    return jsonify(result)


@infoFind.route('/attendInfo', methods=['POST'])
def attendInfo():
    # 获取用户名
    data = json.loads(request.data)
    employee = data.get("username")
    # employee = '20181745'
    if data.get("date"):
        date = datetime.strptime(data.get("date"), '%Y-%m-%d').date()
    else:
        date = datetime.now().date()
    result = aInfo(employee, date)
    return jsonify(result)
