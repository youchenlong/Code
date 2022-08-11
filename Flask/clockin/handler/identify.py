import json

from flask import Blueprint, request, Response, jsonify
from api.identify_api import *

identify = Blueprint('identify', __name__)


@identify.route('/login', methods=['POST'])
def login():
    # 获取用户名和密码
    data = json.loads(request.data)
    username = data.get("username")
    password = data.get("password")
    # username = '20181736'
    # password = '123456'
    result = lgin(username, password)
    return jsonify(result)


@identify.route('/register', methods=['POST'])
def register():
    # 获取用户输入的用户名，密码，电子邮件，姓名，电话号码
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    phone = data.get('phone')
    # username = '20181736'
    # password = '123456'
    # email = 'email'
    # name = 'wdl'
    # phone = '123456789'
    result = reg(username, password, name, phone, email)
    return jsonify(result)
