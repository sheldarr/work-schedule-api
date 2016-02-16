#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return "OK"

@app.route('/shift', methods=['GET'])
def get_shifts():
    with open('./var/shifts.json') as data_file:
        shifts = json.load(data_file)
        return jsonify(shifts)

@app.route('/worker', methods=['GET'])
def get_workers():
    with open('./var/workers.json') as data_file:
        workers = json.load(data_file)
        return jsonify(workers)

if __name__ == '__main__':
    app.run(debug=True)
