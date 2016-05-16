# import os module, lets you run commands on the OS
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(19, GPIO.IN)

print("----------------")
print("  Button + GPIO")
print("----------------")

print(GPIO.input(19))
while True:
        if (GPIO.input(19) == False):
                print ("Button Pressed")
                os.system('date')
                print(GPIO.input(19))
                time.sleep(3)
        else:
                os.system("clear")
                print("Waiting for you to press a button")
time.sleep(1)