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

isOn = False

print GPIO.input(19)
while True:
        if (GPIO.input(19) == False):
                print ("Button Pressed")
                os.system('date')
                print GPIO.input(19)
                if (isOn):
                        GPIO.output(12, GPIO.LOW)
                else:
                        GPIO.output(12, GPIO.HIGH)
                isOn = not isOn
                # time.sleep(0.5)
# else:

# os.system("clear")
# print("Waiting for you to press a button")

time.sleep(1)