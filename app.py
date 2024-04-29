from flask import Flask, render_template, jsonify
from flask_cors import CORS
# from dotenv import load_dotenv
# import os

from views.api import api_bp
from views.register import register_bp
from views.login import login_bp
from views.detection import detection_bp

# load_dotenv()

app = Flask(__name__)
# app.config['CLARIFAI_PAT'] = os.getenv('CLARIFAI_PAT')
# print('CLARIFAI_PAT', app.config['CLARIFAI_PAT']) # 需要整串一起使用

CORS(app)

@app.route('/')
def index():
    # return render_template('index.html')
    return jsonify({'message': 'Hello World from root'})

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(register_bp, url_prefix='/api/register')
app.register_blueprint(login_bp, url_prefix='/signin')
app.register_blueprint(detection_bp, url_prefix='/api/detection')
