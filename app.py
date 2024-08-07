from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/coin_toss', methods=['GET'])
def coin_toss():
    outcome = random.choice(["Kopf", "Zahl"])
    return jsonify(result=outcome)

if __name__ == '__main__':
    app.run(debug=True)
