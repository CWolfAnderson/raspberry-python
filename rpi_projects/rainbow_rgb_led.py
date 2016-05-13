import time
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS = (16, 20, 21)

# set up pins
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

interval = 0.09

# red, yellow, green, cyan, blue, magenta
combinations = ("100", "110", "010", "011", "001", "101")

try:
	while True:
		for combo in combinations:
			GPIO.output(16, int(combo[0]))
			GPIO.output(20, int(combo[1]))
			GPIO.output(21, int(combo[2]))
			time.sleep(interval)

except KeyboardInterrupt:
	GPIO.cleanup()
