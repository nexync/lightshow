import RPi.GPIO as GPIO
import time
import pygame

import patterns as p
import music as m

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinlist = [26,19,13,20,21]

for i in pinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

p.off(pinlist)  

try:
    m.phantoms(1)
    for i in range(4):
        p.alternate(0.5)
    p.(pinlist, 2)
    p.stairup(pinlist, 0.2, 0.1)
    p.stairdown(pinlist, 0.2, 0.1)
