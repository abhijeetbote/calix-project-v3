from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient


app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource="admin")
    
    db = client.developer_db
    return db


@app.route('/')
def ping_server():
    return "welcome to the world of developers"


@app.route('/developers')
def fetch_developers():
    db=""
    try:
        db = get_db()
        _developers = db.developer_tb.find()
        developers = [{"id": developer["id"], "name": developer["name"], "type": developer["type"]} for developer in _developers]
        return jsonify({"developers": developers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.client.close()

# Create a list to act as a simple database.
database = ['ab-list','ab-list2']

# Route for creating a new item.
@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    database.append(data)
    return jsonify(data), 201

# Route for retrieving all items.
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(database)

# Route for updating an item by index.
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.json
    if 0 <= index < len(database):
        database[index] = data
        return jsonify(data)
    return "Item not found", 404
 
# Route for deleting an item by index.
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(database):
        deleted_item = database.pop(index)
        return jsonify(deleted_item)
    return "Item not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
