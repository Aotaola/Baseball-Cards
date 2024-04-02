from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User 

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/login')

def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Login successful', 'user': {'username': user.username, 'email': user.email}})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@user_bp.route('/signup')

def signup():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        bio=data['bio'],
        tokens= 100
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'user': {'username': new_user.username, 'email': new_user.email, 'bio': new_user.bio, 'tokens': new_user.tokens}})

@user_bp.route('/logout')

def logout():


@user_bp.route('/update_user', methods='PATCH')

def update_user():

@user_bp.route('/delete_user', methods='DELETE')

def delete_user():