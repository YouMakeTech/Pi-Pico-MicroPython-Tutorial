# paddleDemo.by
# Pi Pico Retrogaming Console Paddle Demo by YouMakeTech
# Move a paddle with a rotary encoder
#
# Connections:
# ===========
# * Left push button to GP4
# * Right push button to GP5
# * Connect an I2C driven SSD1306 OLED display
#   to pins GP14 (SDA) and GP15 (SCL)
# 
# This code requires the ssd1306.py library to be copied
# to the root directory of the Raspberry Pi Pico.
# If ssd1306.py is not installed, this results in an error:
# "ImportError: no module named 'ssd1306'"
#
# To install the ssd1306.py library
# =================================
# * Download ssd1306.py from https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
# * Open ssd1306.py in Thonny
# * Click on File -> Save as...
# * In the window "Where to save to?", select "Raspberry Pi Pico"

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from rotary import Rotary
import time

# Init I2C using pins GP14 & GP15
i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 400000)

# Init oled display
WIDTH  = 128 # oled display width in pixels
HEIGHT = 64  # oled display height in pixels
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Rotary encoder connected to GP16 and GP17
rotary1 = Rotary(16, 17)
previous_angle = rotary1.get()

# coordinates of the paddle on the screen in pixels
# the screen is 128 pixels wide by 64 pixel high
xp = 60 
yp = 60

while True:
    # clear the screen
    oled.fill(0)
    
    # draw a 16x4 pixels paddle at coordinates (xp,yp)
    oled.fill_rect(xp, yp, 16, 4, 1)
    oled.show()
    
    angle = rotary1.get()
#     print(angle)
    xp += 5*(angle-previous_angle)  # Move the paddle
    previous_angle = angle
        
    time.sleep(0.020)

