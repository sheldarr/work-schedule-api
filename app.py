#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "OK"

@app.route('/shift', methods=['GET'])
def getShifts():
    with open('./var/shifts.json') as data_file:
        shifts = json.load(data_file)
        return jsonify(shifts)

@app.route('/worker', methods=['GET'])
def getWorkers():
    with open('./var/workers.json') as data_file:
        shifts = json.load(data_file)
        return jsonify(shifts)

if __name__ == '__main__':
    app.run(debug=True)
