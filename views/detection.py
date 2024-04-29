from flask import Blueprint, request, jsonify
from controllers.clarifai import detection

detection_bp = Blueprint('api/detection', __name__)

@detection_bp.route('/', methods=['POST'])
def face_detection():
    detection()
    return jsonify({"status": "success"})