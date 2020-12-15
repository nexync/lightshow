import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def cascade(pinlist,onDelay,offDelay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(onDelay)
        GPIO.output(i, GPIO.LOW)
        time.sleep(offDelay)

def stairup(pinlist,stairDelay,offDelay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(stairDelay)
    time.sleep(offDelay)
    for i in pinlist:
        GPIO.output(i, GPIO.LOW)
        time.sleep(stairDelay)

def blink(pinlist,delay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
    time.sleep(delay)
    for i in pinlist:
        GPIO.output(i, GPIO.LOW)

def random(pinlist,delay):
    num = Math.random(len(pinlist))