from flask import Blueprint, request, jsonify, redirect, url_for, session
from app.utils.database import db
#from app.extensions import bcrypt
from app.models.collection import Collection 

collection_bp = Blueprint('collection_bp', __name__)

@collection_bp.route('/collections', methods=['GET'])
def get_collections():
    collections = Collection.query.all()
    return jsonify([{'id': collection.id, 'name': collection.collection_name, 'description': collection.collection_description} for collection in collections])

@collection_bp.route('/collections/<int:collection_id>', methods=['GET'])
def get_collection(collection_id):
    collection = Collection.query.get_or_404(collection_id)
    return jsonify({'id': collection.id, 'name': collection.collection_name, 'description': collection.collection_description, 'tokens': collection.collection_tokens})

@collection_bp.route('/create_collection', methods='POST')
def create_collection():
    data = request.json
    new_collection = Collection(
        collection_name=data['name'],
        collection_description=data['description'],
        user_id=data['user_id']  # Assuming you have a user_id field to link the collection to a user
    )
    db.session.add(new_collection)
    db.session.commit()
    return jsonify({'id': new_collection.id, 'name': new_collection.collection_name, 'description': new_collection.collection_description}), 201

@collection_bp.route('/edit_collection/<int:collection_id>', methods=['PATCH'])
def edit_collection(collection_id):
    collection = Collection.query.get_or_404(collection_id)
    data = request.json
    collection.collection_name = data.get('name', collection.collection_name)
    collection.collection_description = data.get('description', collection.collection_description)
    db.session.commit()
    return jsonify({'id': collection.id, 'name': collection.collection_name, 'description': collection.collection_description})

@collection_bp.route('/delete_collection/<int:collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    collection = Collection.query.get_or_404(collection_id)
    db.session.delete(collection)
    db.session.commit()
    return jsonify({'message': 'Collection deleted'}), 204

