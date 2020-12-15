import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 13
GPIO.setup(ledPin, GPIO.OUT)

try:
	while(True):
		print("LED turning on.")
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.5)
		print("LED turning off.")
		GPIO.output(ledPin, GPIO.LOW) 
		time.sleep(1)

# End program cleanly with keyboard
except KeyboardInterrupt:
    print("Quit")

    # Reset GPIO settings

    GPIO.cleanup()