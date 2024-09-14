import RPi.GPIO as GPIO
import time

relay_pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)

on_off = False

GPIO.output(relay_pin, False)

def relay():
     if on_off:
          GPIO.output(relay_pin, False)
          on_off = False
     else:
          GPIO.output(relay_pin, True)
          on_off = True

for i in range(6):
     relay()


