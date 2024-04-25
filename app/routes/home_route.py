from flask import Blueprint, jsonify
from flask_cors import CORS

home_bp = Blueprint('home_bp', __name__)
CORS(home_bp)

@home_bp.route('/')
def home():
    return 'Hello, world'
