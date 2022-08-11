from flask import Blueprint, jsonify, request

login = Blueprint('login', __name__)

@login.route('/', methods=["GET"])
def check():
    username = request.args.get('username')
    password = request.args.get('password')
    if username=="admin" and password=="admin":
        return jsonify({'code':1})
    return jsonify({'code':0})