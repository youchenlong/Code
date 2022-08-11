"""路由"""

from flask import Blueprint, request, jsonify
from api.test import api_login, api_register

test = Blueprint('test', __name__)

# get请求
@test.route('/login', methods=["GET"])
def login():
    data = request.args
    id = data.get('id')
    result = api_login(id)
    return jsonify(result)

# post请求
@test.route('/register', methods=['POST'])
def register():
    data = request.form
    id = data.get('id')
    name = data.get('name')
    sex = data.get('sex')
    phone = data.get('phone')
    email = data.get('email')
    result = api_register(id, name, sex, phone, email)
    return jsonify(result)
    
# get请求
@test.route('/getUrl', methods=["GET"])
def getUrl():
    data = request.args
    p = data.get('p')
    """
        此处省略逻辑操作
    """
    result = {'code': 200, '_url': 'http://xxxxxx'}
    return jsonify(result)