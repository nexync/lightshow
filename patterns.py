import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def off(pinlist):
    for i in pinlist:
        GPIO.output(i,GPIO.LOW)

def on(pinlist):
    for i in pinlist:
        GPIO.output(i,GPIO.HIGH)

def cascade(pinlist,onDelay,offDelay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(onDelay)
        GPIO.output(i, GPIO.LOW)
        if i != pinlist[-1]:
            time.sleep(offDelay)

def stairup(pinlist,stairDelay,offDelay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(stairDelay)
    time.sleep(offDelay)
    for i in pinlist:
        GPIO.output(i, GPIO.LOW)
        if i != pinlist[-1]:
            time.sleep(stairDelay)

def stairdown(pinlist,stairDelay,offDelay):
    for i in reversed(pinlist):
        GPIO.output(i, GPIO.HIGH)
        time.sleep(stairDelay)
    time.sleep(offDelay)
    for i in reversed(pinlist):
        GPIO.output(i, GPIO.LOW)
        if i != pinlist[0]:
            time.sleep(stairDelay)

def blink(pinlist,delay):
    for i in pinlist:
        GPIO.output(i, GPIO.HIGH)
    time.sleep(delay)
    for i in pinlist:
        GPIO.output(i, GPIO.LOW)

def alternate(pinlist,switchDelay):
    for i in range(len(pinlist)):
        if i % 2 == 0:
            GPIO.output(pinlist[i],GPIO.HIGH)
    time.sleep(switchDelay)
    for i in range(len(pinlist)):
        if i % 2 == 1:
            GPIO.output(pinlist[i],GPIO.HIGH)
        if i % 2 == 0:
            GPIO.output(pinlist[i],GPIO.LOW)
    time.sleep(switchDelay)
    for i in range(len(pinlist)):
        if i % 2 == 1:
            GPIO.output(pinlist[i],GPIO.LOW)


def random(pinlist,delay):
    num = Math.random(len(pinlist))

# pinlist = [26,19,13,20,21]
def closein(pinlist, timeon, sleeptime):
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[4], GPIO.HIGH)
    time.sleep(timeon)
    GPIO.output(pinlist[0],GPIO.LOW)
    GPIO.output(pinlist[4],GPIO.LOW)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[3], GPIO.HIGH)
    time.sleep(timeon)
    GPIO.output(pinlist[1],GPIO.LOW)
    GPIO.output(pinlist[3],GPIO.LOW)
    GPIO.output(pinlist[2],GPIO.HIGH)
    time.sleep(timeon)
    GPIO.output(pinlist[2],GPIO.LOW)

def flashb3(pinlist, timeon, timeoff):
    GPIO.output(pinlist[3],GPIO.LOW)
    GPIO.output(pinlist[4],GPIO.LOW)
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timeon)
    GPIO.output(pinlist[0],GPIO.LOW)
    GPIO.output(pinlist[1],GPIO.LOW)
    GPIO.output(pinlist[2],GPIO.LOW)
    time.sleep(timeoff)



def switchsides(pinlist,timeon):
    GPIO.output(pinlist[3],GPIO.LOW)
    GPIO.output(pinlist[4],GPIO.LOW)
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timeon)
    GPIO.output(pinlist[0],GPIO.LOW)
    GPIO.output(pinlist[1],GPIO.LOW)
    GPIO.output(pinlist[2],GPIO.LOW)
    GPIO.output(pinlist[3],GPIO.HIGH)
    GPIO.output(pinlist[4],GPIO.HIGH)
    time.sleep(timeon)

def buildin(pinlist, timesleep):
    
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[4], GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[3],GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timesleep)

def buildout(pinlist,timesleep):
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[3],GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[4], GPIO.HIGH)
    time.sleep(timesleep)
    
def collapsein(pinlist, timeon):
    GPIO.output(pinlist[0], GPIO.HIGH)
    GPIO.output(pinlist[4], GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[0], GPIO.LOW)
    GPIO.output(pinlist[4], GPIO.LOW)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[3],GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[1], GPIO.LOW)
    GPIO.output(pinlist[3],GPIO.LOW)
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timesleep)

def collapseout(pinlist,timeon):
    GPIO.output(pinlist[2], GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[2], GPIO.LOW)
    GPIO.output(pinlist[1], GPIO.HIGH)
    GPIO.output(pinlist[3],GPIO.HIGH)
    time.sleep(timesleep)
    GPIO.output(pinlist[1], GPIO.LOW)
    GPIO.output(pinlist[3],GPIO.LOW)
    GPIO.output(pinlist[4], GPIO.HIGH)
    GPIO.output(pinlist[0], GPIO.HIGH)
    time.sleep(timesleep)
