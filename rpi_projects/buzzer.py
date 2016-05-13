import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up pin
GPIO.setup(19, GPIO.OUT)

def beep(number_of_times):

	beep_time = 0.2
	time_in_between_beeps = 0.2

	for i in range(number_of_times):
		GPIO.output(19, GPIO.HIGH)
		time.sleep(beep_time)
		GPIO.output(19, GPIO.LOW)
		time.sleep(time_in_between_beeps)

finished = False

try:
	while not finished:
		input = raw_input("Enter number of beeps (q to quit): ")
		if input.isdigit():
			beep(int(input))
		else:
			finished = True

except KeyboardInterrupt:
	GPIO.cleanup()

GPIO.cleanup()
