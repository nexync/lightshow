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
    for i in range(5):
        p.alternate(pinlist, 0.45)
    p.blink(pinlist, 2.75)
    p.stairdown(pinlist, 0.25, 0.1)
    GPIO.output(pinlist[4],GPIO.LOW)
    time.sleep(1)
    p.stairup(pinlist, 0.25, 0.1)
    GPIO.output(pinlist[0],GPIO.LOW)

    GPIO.cleanup()


#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()