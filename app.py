from flask import Flask, escape
from flask_cors import CORS
import RPi.GPIO as GPIO
from time import sleep

servoPIN = 17
GPIO.setMode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM @ 50hz
pwm.start(0)  # Initialization

app = Flask(__name__)
CORS(app)


def SetAngle(angle):
    duty = angle/18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0)


@app.route('/')
def index():
    return 'Home'


@app.route('/user/<user>', methods=['GET', 'POST'])
def user(user):
    return {'user': escape(user)}


@app.route('/bootprinter', methods=['GET'])
def bootprinter_status():
    print("Check things aren't broken....")
    return {'status': 'OK'}


@app.route('/bootprinter', methods=['POST'])
def bootprinter_execute():
    print("Boot Printer servo code....")
    return ('', 204)


@app.route('/bootpc', methods=['GET'])
def bootpc_status():
    print("Check things aren't broken....")
    return {'status': 'OK'}


@app.route('/bootpc', methods=['POST'])
def bootpc_execute():
    print("Boot PC servo code....")
    SetAngle(90)
    sleep(2)
    SetAngle(0)
    sleep(2)
    return ('', 204)
