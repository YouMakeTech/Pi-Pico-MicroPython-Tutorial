# oledTest.py:  I2C SSD1306 OLED Test by YouMakeTech
# 
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
# Now run oledTest.py
#
# Documentation
# =============
# * https://github.com/raspberrypi/pico-micropython-examples/tree/master/i2c/1306oled
# * https://docs.micropython.org/en/latest/library/framebuf.html

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

# Init I2C using pins GP14 & GP15
i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 400000)     

# Init oled display
WIDTH  = 128 # oled display width in pixels
HEIGHT = 64  # oled display height in pixels
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  

# Fill the screen with white
oled.fill(1)
oled.show()
time.sleep(1)

# Clear the screen (fill with "black")
oled.fill(0)
oled.show()
time.sleep(1)

# Draw a white pixel at the top left corner
# The top left corner has coordinates (0,0)
# Python counts from zero, not one!
oled.pixel(0, 0, 1)
oled.show()
time.sleep(1)

# Draw a white pixel at the bottom right corner.
# The bottom right corner has coordinates (127,63)
oled.pixel(127, 63 , 1)
oled.show()
time.sleep(1)

# Draw a line from the top left to the bottom right corner
oled.line(0, 0, 127, 63, 1)
oled.show()
time.sleep(1)

# Draw a rectangle: the top left corner is at X=32 and Y=48.
# The width of the rectangle is 16 and its height is 4 pixels
oled.rect(32, 48, 16, 4, 1)
oled.show()
time.sleep(1)

# Same as above but fill the interior
oled.fill_rect(32, 48, 16, 4, 1)
oled.show()
time.sleep(1)

# Display some text
oled.text("YouMakeTech",8,8)
oled.show()
time.sleep(1)

# Vertical Scrolling
import random
for i in range(63):
    oled.scroll(0, 1) # scroll the screen down by one pixel
    oled.line(0, 0, 127, 0, 0) # fill the first row with black
    oled.pixel(random.randint(0,127), 0, 1) # display a random star on the first row
    oled.show()
    time.sleep(0.010)
    
# Display an image 
# Space Invaders sprite as array of 8x8 bits (= 8 bytes)
image = bytearray([0b00011000,
                   0b00111100,
                   0b01111110,
                   0b11011011,
                   0b11111111,
                   0b00100100,
                   0b01011010,
                   0b10100101])

# Load the image into a framebuffer (the image is 8x8)
fb = framebuf.FrameBuffer(image, 8, 8, framebuf.MONO_HLSB)

# Draw the image at coordinates X=96 and Y=0
oled.blit(fb, 96, 0) 
oled.show()
time.sleep(1)
