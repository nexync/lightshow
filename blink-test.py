for i in range(5):
	print("LED turning on.")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(0.5)
	print("LED turning off.")
	GPIO.output(ledPin, GPIO.LOW) 
	time.sleep(0.5)