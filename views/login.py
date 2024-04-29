from flask import Blueprint, request, jsonify
from controllers.login import user_login

login_bp = Blueprint('signin', __name__)

@login_bp.route('', methods=['POST'])
def login():
    print('login')
    return user_login()