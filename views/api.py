from flask import Blueprint, request, jsonify
from controllers.register import register_user

api_bp = Blueprint('api', __name__)

@api_bp.route('/endpoint1')
def endpoint1():
    return 'This is endpoint 1'

@api_bp.route('/endpoint2')
def endpoint2():
    return 'This is endpoint 2'

@api_bp.route('/get_data', methods=['GET'])
def get_data():
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
