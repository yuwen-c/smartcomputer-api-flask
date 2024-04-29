from flask import Blueprint, request, jsonify
from controllers.register import register_user

register_bp = Blueprint('api/register', __name__)

@register_bp.route('/', methods=['POST'])
def register():
    return register_user()