import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 26
led2Pin = 19
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(led2Pin ,GPIO.OUT)

try:
	while(True):
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(1.5)
		GPIO.output(led2Pin,GPIO.HIGH)
		time.sleep(1.5)
		GPIO.output(led2Pin, GPIO.LOW) 
		time.sleep(0.5)
		GPIO.output(ledPin,GPIO.LOW)
		time.sleep(0.5)

# End program cleanly with keyboard
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()