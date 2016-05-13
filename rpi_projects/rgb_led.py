import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = (16, 20, 21)

# set up pins
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

finished = False

print("Enter color in format ### with 1's and/or 0's referring Red, Green, and Blue respectively.")
print("Enter anything else to quit.")

try:
	while not finished:
		input = raw_input("RGB: ")
		if len(input) == 3:
			GPIO.output(16,int(input[0]))
			GPIO.output(20,int(input[1]))
			GPIO.output(21,int(input[2]))
		else:
			finished = True

except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
