# import os module, lets you run commands on the OS
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
# button pin
GPIO.setup(19, GPIO.IN)
# led pin
GPIO.setup(12, GPIO.OUT)

print("----------------")
print("  Button + GPIO")
print("----------------")

print GPIO.input(19)
while True:
        if (GPIO.input(19) == False):
                print ("Button Pressed")
                os.system('date')
                print GPIO.input(19)
                GPIO.output(12, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(12, GPIO.LOW)
        else:
                os.system("clear")
                print("Waiting for you to press a button")
time.sleep(1)