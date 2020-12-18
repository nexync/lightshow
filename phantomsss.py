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
    m.phantom(0)
    for i in range(4):
        p.alternate(pinlist, 0.45)
    time.sleep(0.65)
    p.blink(pinlist, 2.75)
    p.stairdown(pinlist, 0.25, 0.1)
    p.stairup(pinlist, 0.25, 0.1)

    GPIO.cleanup()


#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()