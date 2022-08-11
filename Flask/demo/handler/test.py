from flask import Blueprint, jsonify

test = Blueprint('test', __name__)

@test.route('/getJson', methods=["GET"])
def getJson():
    return jsonify({'a':1, 'b':2})