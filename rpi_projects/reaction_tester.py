import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# button pin
GPIO.setup(26, GPIO.IN)

# buzzer pin
GPIO.setup(18, GPIO.OUT)

# led pins
PINS = (4, 17, 27, 22, 5, 6, 13, 19)

# set up pins
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

# if there is a winner
def winner(delay, blink_count):
	for i in range(blink_count):
		for pin in PINS:
			GPIO.output(pin, GPIO.HIGH)
			
		time.sleep(delay)
		
		for pin in PINS:
			GPIO.output(pin, GPIO.LOW)

		time.sleep(delay)

speed = 0.5
beep_time = 0.25
counter = 0

try:
	while True:
		for pin in PINS:
			GPIO.output(pin, GPIO.HIGH)
			time.sleep(speed)
			GPIO.output(pin, GPIO.LOW)
			if GPIO.input(26) == False:
				print("Button Pressed")
				os.system('date')
				print(GPIO.input(26))
				if pin == 5:
					# we have a winner
					winner(0.3, 3)
					if counter == 9:
						# reset the speed
						speed = 0.5
						winner(0.125, 10)
					else:
						speed -= 0.05
					counter += 1
				else:
					# sound buzzer
					GPIO.output(18, GPIO.HIGH)
					time.sleep(beep_time)
					GPIO.output(18, GPIO.LOW)
			else:
				os.system("clear")
				print("Waiting for you to press a button")
				# time.sleep(1)		

except KeyboardInterrupt:
	GPIO.cleanup()
