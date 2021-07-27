import PRi.GPIO as GPIO
from time import sleep

servoPIN = 17
GPIO.setMode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM @ 50hz
pwm.start(0)  # Initialization


def SetAngle(angle):
    duty = angle/18 + 2
    GPIO.output(servoPIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    pwm.ChangeDutyCycle(0)


try:
    while True:
        SetAngle(90)
        sleep(2)
        SetAngle(0)
        sleep(2)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
