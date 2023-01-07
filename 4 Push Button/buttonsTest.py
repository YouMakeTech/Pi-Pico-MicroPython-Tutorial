# buttonsTest.py
# Pi Pico Retrogaming Console Push Buttons Test by YouMakeTech
# Connect push buttons to the Pico like this:
# Up to GP2
# Down to GP3
# Left to GP4
# Right to GP5
# Button A to GP6
# Button B to GP7

from machine import Pin
import time

up = Pin(2, Pin.IN, Pin.PULL_UP)
down = Pin(3, Pin.IN, Pin.PULL_UP)
left = Pin(4, Pin.IN, Pin.PULL_UP)
right = Pin(5, Pin.IN, Pin.PULL_UP)
button1 = Pin(6, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)

print("Press any button...")
time.sleep(2)

while True:
    if up.value() == 0:
        print("UP Button Pressed")
    if down.value() == 0:
        print("DOWN Button Pressed")
    if left.value() == 0:
        print("LEFT Button Pressed")
    if right.value() == 0:
        print("RIGHT Button Pressed")
    if button1.value() == 0:
        print("Button A Pressed")
    if button2.value() == 0:
        print("Button B Pressed")
    time.sleep(0.040)
