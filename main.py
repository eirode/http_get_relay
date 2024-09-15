from flask import Flask
import RPi.GPIO as GPIO
import time

etat = False
verif_var = 0

relay_pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, False)


def relay():
    global etat
    if etat:
        GPIO.output(relay_pin, False)
        etat = False
    else:
        GPIO.output(relay_pin, True)
        etat = True


app = Flask(__name__)


@app.route('/')
def hello():
    relay()
    return "hello from the Raspberry Pi!"


app.run(host='0.0.0.0', port= 8090)
