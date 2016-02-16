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
    with open('./data/shifts.json') as data_file:
        shifts = json.load(data_file)
        return jsonify(shifts)

@app.route('/worker', methods=['GET'])
def get_workers():
    with open('./data/workers.json') as data_file:
        workers = json.load(data_file)
        return jsonify(workers)

@app.route('/worker/<int:worker_id>', methods=['DELETE'])
def delete_worker(worker_id):
    with open('./data/workers.json') as data_file:
        data = json.load(data_file)
        workers = data["workers"]
        print (workers)
        for i in range(len(workers)):
            if workers[i]["id"] == worker_id:
                workers.pop(i)
                break
        print(workers)
        open("./data/workers_test.json", "w").write(
            json.dumps(workers, sort_keys=True, indent=4, separators=(',', ': '))
        )
        return "OK"

if __name__ == '__main__':
    app.run(debug=True)
