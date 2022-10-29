from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user_info/')
def get_user_info():
    return jsonify({'slackUsername':'tshergzeh',
                    'backend':True,
                    'age':21,
                    'bio':'I am a backend developer participating in the HNG9 internship.'})

@app.route('/')
def hello_world():
    return 'Hello World!'

