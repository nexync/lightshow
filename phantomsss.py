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
    m.phantom(27)
    # for i in range(5):
    #     p.alternate(pinlist, 0.45)
    # p.blink(pinlist, 2.75)
    # p.stairdown(pinlist, 0.25, 0.1)
    # GPIO.output(pinlist[4],GPIO.LOW)
    # time.sleep(1.35)
    # p.stairup(pinlist, 0.23, 0.1)
    # GPIO.output(pinlist[0],GPIO.LOW)
    # for i in range(2):
    #     p.cascade(pinlist,0.23, 0.01)
    # for i in range(1):
    #     p.stairup(pinlist, 0.35, 0.1)
    # GPIO.output(pinlist[0],GPIO.LOW)
    # p.blink(pinlist, 1.8)
    # for i in range(12):
    #     p.switchsides(pinlist, 0.2225)
    for i in range(4):
        p.flashb3(pinlist, 0.23)
        p.buildin(pinlist, 0.23)
        p.buildout(pinlist,0.23)
    for i in range(4):
        p.collapsein(pinlist, 0.225)
        p.collapseout(pinlist, 0.225)
    for i in range(2):
        p.flashb3(pinlist, 0.23)
        p.buildin(pinlist, 0.23)
        p.buildout(pinlist,0.23)
    for i in range(2):
        p.collapsein(pinlist, 0.225)
        p.collapseout(pinlist, 0.225)
    GPIO.output(pinlist[4],GPIO.LOW)
    GPIO.output(pinlist[0],GPIO.LOW)
    p.cascade(pinlist, 0.23, 0.05)
    GPIO.output(pinlist[4],GPIO.LOW)
    GPIO.output(pinlist[0],GPIO.LOW)
    p.cascade(pinlist, 0.23, 0.05)
    GPIO.output(pinlist[0],GPIO.LOW)
    GPIO.output(pinlist[4],GPIO.LOW)
    for i in range(2):
        p.cascade(pinlist,0.23, 0.05)
    for i in range(5):
        p.alternate(pinlist, 0.23)
    time.sleep(0.3)
    for i in range(3):
        p.blink(pinlist, 0.2)
        time.sleep(0.05)
    time.sleep(0.23)
    for i in range(2):
        p.collapsein(pinlist, 0.225)
        p.collapseout(pinlist, 0.225)
    for i in range(1):
        p.stairup(pinlist, 0.35, 0.1)
    
    GPIO.cleanup()



#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()