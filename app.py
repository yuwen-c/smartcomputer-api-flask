from flask import Flask, render_template, jsonify
from flask_cors import CORS

from views.api import api_bp
from views.register import register_bp

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # return render_template('index.html')
    return jsonify({'message': 'Hello World from root'})

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(register_bp, url_prefix='/api/register')
