import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 13
GPIO.setup(ledPin, GPIO.OUT)

try:
	while(True):
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.25)
		GPIO.output(ledPin, GPIO.LOW) 
		time.sleep(1)
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(ledPin, GPIO.LOW) 
		time.sleep(1.25)

# End program cleanly with keyboard
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()