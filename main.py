import RPi.GPIO as GPIO
import time
import pygame

import patterns as p
import music as m

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinlist = [26,19,13,20,21]


#SETUP PINS
for i in pinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)  #so default value of lights is on


#ACTIONS 
p.off(pinlist)                 #set all lights to off initially

try:
    m.sleigh()
    for i in range(10):
        p.cascade(pinlist,0.25,0.1)
        time.sleep(0.5)
        p.blink(pinlist,0.5)
        time.sleep(0.5)
        p.stairup(pinlist,0.1,0.5)
        p.stairdown(pinlist,0.1,0.5)
        time.sleep(1)
        p.alternate(pinlist,0.3)
    GPIO.cleanup()


#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()