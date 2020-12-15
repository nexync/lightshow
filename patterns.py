import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def cascade(pinlist):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(i, GPIO.LOW)
        time.sleep(0.25)

def stairup(pinlist):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(0.1)
    time.sleep(1)
    for i in pinlist:
        GPIO.output(i, GPIO.LOW)
        time.sleep(0.1)