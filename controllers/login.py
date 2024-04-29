from flask import jsonify, request
from models.logins import get_user

def user_login():
  request_data = request.get_json()
  email = request_data.get('email')
  password = request_data.get('password')
  if not email or not password:
    return jsonify({'error': 'Missing required fields'}), 400

  try:
    result = get_user(email)
    print('get user result', result) # ('johnny3@gmail.com', 'Johnny3', '12345')
    # 比對密碼
    if result and result[2] == password:
      return jsonify({
        'status': 'login success',
        'name': result[1],
        'email': result[0]
      })
    elif result:
      return jsonify({'error': 'Invalid password'}), 400
    else:
      return jsonify({'error': 'User not found'}), 404
  except Exception as e:
    print('user_login', e)
    return jsonify({'error': 'An error occurred while logging in'}), 500