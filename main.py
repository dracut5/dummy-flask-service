#!/usr/bin/env python


import flask
import os
import time
import random

SERVICE_ROLE = os.environ.get('SERVICE_ROLE', 'blue')
APP_PATH_PREFIX = '/app'

with open(APP_PATH_PREFIX + '/files/picture.png', 'rb') as file:
    data = file.read()

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    #time.sleep(60)
    #response_code = random.choice([200, 200, 500, 503, 504])
    return f'Hello World!I am {SERVICE_ROLE}.\n'

@app.route('/status')
def status():
    return 'Status OK\n'

@app.route('/metrics')
def metrics():
    return 'Metrics OK\n'

@app.route('/picture')
def get_file():
    resp = flask.Response(data, status = 200, mimetype='image/png')
    return resp
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
