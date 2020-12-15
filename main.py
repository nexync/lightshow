import RPi.GPIO as GPIO
import time

import patterns as p

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinlist = [26,19,13,20,21]


#SETUP PINS
for i in pinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

p.cascade(pinlist,0.2,0.1)
p.cascade(pinlist,0.2,0.1)
p.stairup(pinlist,0.1,1)
p.blink(pinlist,0.5)