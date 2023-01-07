# ballDemo.py: Pi Pico Retrogaming Console ball Demo by YouMakeTech
# Move a ball like in the game Pong.
# Show how to use the OLED display to make animations
#
# Connections
# ===========
# Connect an I2C driven SSD1306 OLED display
# to pins GP14 (SDA) and GP15 (SCL)
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
#

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Init I2C using pins GP14 & GP15
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq = 400000)     

# Init oled display
WIDTH  = 128 # oled display width in pixels
HEIGHT = 64  # oled display height in pixels
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  

# Simple Pong
x = 64 # ball coordinates on the screen in pixels
y = 0
vx = 2 # ball velocity along x and y in pixels per frame
vy = 2
while True:
    # Clear the screen
    oled.fill(0)
    
    # Draw a 4x4 pixels ball at (x,y) in white
    oled.fill_rect(x, y, 4, 4, 1)
    oled.show()
    
    # Move the ball by adding the velocity vector
    x += vx
    y += vy
    
    # Make the ball rebound on the edges of the screen
    if x < 0:
        x = 0
        vx = -vx
    if y < 0:
        y = 0
        vy = -vy
    if x + 4 > 128:
        x = 128 - 4
        vx = -vx
    if y + 4 > 64:
        y = 64 - 4
        vy = -vy
