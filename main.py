#!/usr/bin/env python


import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/status')
def status():
    return 'Status OK\n'

@app.route('/metrics')
def metrics():
    return 'Metrics OK\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
