import datetime
import json

from flask import Blueprint, request, Response, jsonify
from api.faceID_api import *

faceID = Blueprint('faceID', __name__)


@faceID.route('/faceInfoInput', methods=['POST'])
def faceInfoInput():
    # 获取用户名和密码
    data = json.loads(request.data)
    username = data.get("username")
    password = data.get("password")
    # username = '20181745'
    # password = '123456'
    result = fInfoInput(username, password)
    return jsonify(result)


@faceID.route('/clockin')
def clockin():
    # 从客户端获取用户名
    username = request.args.get("username")
    # username = '20181745'
    date = datetime.today().date()
    result = cin(username, date)
    return jsonify(result)


@faceID.route('/jump')
def jump():
    url = "10.236.66.15:8080/#/"
    return jsonify({'code': 0, 'message': url})
