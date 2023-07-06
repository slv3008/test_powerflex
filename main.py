import json
from flask import Flask, request, jsonify, abort
from models import db, Factory, Sprocket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/factories', methods=['GET'])
def get_factories():
    with open('data/seed_factory_data.json') as file:
        factories_data = json.load(file)
    return jsonify(factories_data)

@app.route('/factories/<int:id>', methods=['GET'])
def get_factory(id):
    with open('data/seed_factory_data.json') as file:
        factories_data = json.load(file)['factories']
    
    if id < 0 or id >= len(factories_data):
        abort(404)

    return jsonify(factories_data[id])

@app.route('/sprockets/<int:id>', methods=['GET'])
def get_sprocket(id):
    with open('data/seed_sprocket_types.json') as file:
        sprockets_data = json.load(file)['sprockets']

    if id < 0 or id >= len(sprockets_data):
        abort(404)
    
    return jsonify(sprockets_data[id])

@app.route('/sprockets', methods=['POST'])
def create_sprocket():
    data = request.get_json()

    if not data:
        abort(400)
    
    with open('data/seed_sprocket_types.json', 'r+') as file:
        sprockets_data = json.load(file)
        sprockets_data['sprockets'].append(data)
        file.seek(0)
        json.dump(sprockets_data, file)
        file.truncate()
    
    return jsonify(data), 201

@app.route('/sprockets/<int:id>', methods=['PUT'])
def update_sprocket(id):
    data = request.get_json()

    if not data:
        abort(400)

    with open('data/seed_sprocket_types.json', 'r+') as file:
        sprockets_data = json.load(file)

        if id < 0 or id >= len(sprockets_data['sprockets']):
            abort(404)

        sprockets_data['sprockets'][id] = data
        file.seek(0)
        json.dump(sprockets_data, file)
        file.truncate()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
