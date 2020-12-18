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
    m.sleigh(16)
    # first 15 seconds
    # for i in range(4):
    #     p.alternate(pinlist, 0.635)
    # p.blink(pinlist, 0.75)
    # p.cascade(pinlist,0.25,0.1)
    # p.blink(pinlist, 0.75)
    # time.sleep(0.4)
    # for i in range(3):
    #     p.blink(pinlist, 0.2)
    #     time.sleep(0.10)
    # time.sleep(0.5)
    # p.stairup(pinlist,0.1,0.5)
    # time.sleep(0.5)
    # p.stairdown(pinlist,0.1,0.5)
    # time.sleep(0.32)
    # for i in range(3):
    #     p.blink(pinlist, 0.2)
    #     time.sleep(0.10)
    for i in range(2):
        p.alternate(pinlist, 0.635)
    for i in range (2):
        p.cascade(pinlist,0.2,0.1)
    p.closein(pinlist, 0.35, 0.1)
    p.alternate(pinlist, 0.35)
    p.closein(pinlist, 0.5, 0.1)
    for i in range (3):
        p.blink(pinlist, 0.25)
        time.sleep(0.1)
    for i in range(2):
        p.alternate(pinlist, 0.5)
    GPIO.output(pinlist[4], GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(pinlist[3], GPIO.HIGH)
    time.sleep(0.65)
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(0.45)
    GPIO.output(pinlist[1],GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(pinlist[0],GPIO.HIGH)
    
    p.stairup(pinlist, 0.2, 0.5)
    p.stairdown(pinlist, 0.2, 0.5)




    # for i in range(10):
    #     p.cascade(pinlist,0.25,0.1)
    #     time.sleep(0.5)
    #     p.blink(pinlist,0.5)
    #     time.sleep(0.5)
    #     p.stairup(pinlist,0.1,0.5)
    #     time.sleep(0.25)
    #     p.stairdown(pinlist,0.1,0.5)
    #     time.sleep(1)
    #     p.alternate(pinlist,0.3)
    GPIO.cleanup()


#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()