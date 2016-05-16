import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# button pin
GPIO.setup(26, GPIO.IN)

# led pins
PINS = (4, 17, 27, 22, 5, 6, 13, 19)

# set up pins
for pin in PINS:
	GPIO.setup(pin, GPIO.OUT)

print(GPIO.input(26))

while True:
        if (GPIO.input(26) == False):
                print("Button Pressed")
                os.system('date')
                print(GPIO.input(26))
                GPIO.output(4, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(4, GPIO.LOW)
        else:
                os.system("clear")
                print("Waiting for you to press a button")
time.sleep(1)