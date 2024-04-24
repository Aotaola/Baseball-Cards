from flask import Blueprint, jsonify

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return 'Hello, world'