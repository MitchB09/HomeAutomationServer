from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home'


@app.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    return {'user': escape(user)}


@app.route('/bootpc', methods=['GET'])
def bootpc_status():
    print("Check things aren't broken....")
    return {'status': 'OK'}


@app.route('/bootpc', methods=['POST'])
def bootpc_execute():
    print("Boot PC servo code....")
    return ('', 204)
