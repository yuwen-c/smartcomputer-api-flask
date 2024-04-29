from flask import jsonify, request
from models.logins import insert_user

def register_user():
  request_data = request.get_json()
  name = request_data.get('name')
  email = request_data.get('email')
  password = request_data.get('password')
  if not name or not email or not password:
    return jsonify({'error': 'Missing required fields'}), 400

  try:
    result = insert_user(name, email, password)
    return jsonify(result)
  except Exception as e:
    print('register_user', e)
    return jsonify({'error': 'An error occurred while registering user'}), 500
