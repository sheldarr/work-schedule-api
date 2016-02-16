#!flask/bin/python
from flask import Flask, jsonify, request
from flask.ext.cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'OK', 200

@app.route('/shift', methods=['GET'])
def get_shifts():
    with open('./data/shifts.json') as data_file:
        shifts = json.load(data_file)
        return jsonify(shifts)

@app.route('/shift', methods=['POST'])
def create_shift():
    if not request.json:
        abort(400)

    with open('./data/shifts.json') as data_file:
        data = json.load(data_file)
        shifts = data['shifts']

        shift = {
            'id': max(shift['id'] for shift in shifts) + 1,
            'name': request.json['name'],
            'startHour': request.json['startHour'],
            'startMinute': request.json['startMinute'],
            'endHour': request.json['endHour'],
            'endMinute': request.json['endMinute']
        }

        shifts.append(shift)

        open('./data/shifts.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

@app.route('/shift/<int:shift_id>', methods=['DELETE'])
def delete_shift(shift_id):
    with open('./data/shifts.json') as data_file:
        data = json.load(data_file)
        shifts = data['shifts']

        for i in range(len(shifts)):
            if shifts[i]['id'] == shift_id:
                shifts.pop(i)
                break

        open('./data/shifts.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

@app.route('/worker', methods=['GET'])
def get_workers():
    with open('./data/workers.json') as data_file:
        workers = json.load(data_file)
        return jsonify(workers)

@app.route('/worker', methods=['POST'])
def create_worker():
    if not request.json:
        abort(400)

    with open('./data/workers.json') as data_file:
        data = json.load(data_file)
        workers = data['workers']

        worker = {
            'id': max(worker['id'] for worker in workers) + 1,
            'name': request.json['name'],
            'schedule': []
        }

        workers.append(worker)

        open('./data/workers.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

@app.route('/worker/<int:worker_id>', methods=['DELETE'])
def delete_worker(worker_id):
    with open('./data/workers.json') as data_file:
        data = json.load(data_file)
        workers = data['workers']

        for i in range(len(workers)):
            if workers[i]['id'] == worker_id:
                workers.pop(i)
                break

        open('./data/workers.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

@app.route('/worker/<int:worker_id>/shiftLink', methods=['POST'])
def link_shift(worker_id):
    if not request.json:
        abort(400)

    with open('./data/workers.json') as data_file:
        data = json.load(data_file)
        workers = data['workers']

        shiftLink = {
            'dayOfYear': request.json['dayOfYear'],
            'shiftId': int(request.json['shiftId'])
        }

        for i in range(len(workers)):
            if workers[i]['id'] == worker_id:
                workers[i]['schedule'].append(shiftLink)
                break

        open('./data/workers.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

@app.route('/worker/<int:worker_id>/shiftLink/<int:day_of_year>', methods=['DELETE'])
def unlink_shift(worker_id, day_of_year):
    with open('./data/workers.json') as data_file:
        data = json.load(data_file)
        workers = data['workers']

        for i in range(len(workers)):
            if workers[i]['id'] == worker_id:
                for j in range(len(workers[i]['schedule'])):
                    if workers[i]['schedule'][j]['dayOfYear'] == day_of_year:
                        workers[i]['schedule'].pop(j)
                        break
            break

        open('./data/workers.json', 'w').write(
            json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        )

        return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
