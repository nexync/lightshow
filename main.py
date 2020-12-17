import RPi.GPIO as GPIO
import time

import patterns as p

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
    for i in range(10):
        p.cascade(pinlist,0.25,0.1)
        time.sleep(0.5)
    GPIO.cleanup()


#Clean Quit from program - resets all lights
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()