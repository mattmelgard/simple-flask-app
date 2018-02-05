import socket
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/hostname/')
def hostname():
    return socket.gethostname()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
