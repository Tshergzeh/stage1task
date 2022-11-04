from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/user_info/')
def get_user_info():
    return jsonify({'slackUsername':'tshergzeh',
                    'backend':True,
                    'age':21,
                    'bio':'I am a backend developer participating in the HNG9 internship.'})

@app.route('/operate', methods=['POST'])
def operate():
    if not request.json or not 'operation_type' in request.json or not 'x' in request.json or not 'y' in request.json:
        abort(400)
    operation = {
        'operation_type': request.json['operation_type'],
        'x': request.json['x'],
        'y': request.json['y']
    }
    if operation['operation_type'] == 'addition':
        result = operation['x'] + operation['y']
    elif operation['operation_type'] == 'subtraction':
        result = operation['x'] - operation['y']
    elif operation['operation_type'] == 'multiplication':
        result = operation['x'] * operation['y']
    else:
        abort(400)
    return jsonify({'slackUsername': 'tshergzeh',
        'operation_type': operation['operation_type'],
        'result': result
    })

@app.route('/')
def hello_world():
    return 'Hello World!'

