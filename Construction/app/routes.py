from flask import jsonify, request
from app import app, db
from app.models import Item

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify({'items': [{'name': item.name, 'description': item.description} for item in items]})

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created successfully'})

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({'name': item.name, 'description': item.description})

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data['name']
    item.description = data.get('description')
    db.session.commit()
    return jsonify({'message': 'Item updated successfully'})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})
