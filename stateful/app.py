from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_id = str(uuid.uuid4())
    users[user_id] = {'username': data['username'], 'password': data['password']}
    return jsonify({'user_id': user_id}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    for user_id, user in users.items():
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({'message': 'Login successful', 'user_id': user_id}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
