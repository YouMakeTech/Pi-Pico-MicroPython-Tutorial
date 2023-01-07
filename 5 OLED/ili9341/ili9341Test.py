from machine import Pin, SPI
from ili9341 import ILI9341, color565
from time import sleep

spi = SPI(1, sck = Pin(14), mosi = Pin(15), baudrate = 40000000)
display = ILI9341(320, 240, spi, dc = Pin(12), rst = Pin(11), cs = Pin(13))

# fill screen
display.clear() # Black
sleep(1)
display.clear(color565(255, 0, 0)) # Red
sleep(1)
display.clear(color565(0, 255, 0)) # Green
sleep(1)
display.clear(color565(0, 0, 255)) # Blue
sleep(1)

# lines
# (0,0) = top left corner to (319,239) = bottom right corner
display.draw_line(0, 0, 319, 239, color565(255, 255, 0))

display.draw_rectangle(0, 0, 160, 160, color565(255, 0, 255))
sleep(1)

display.invert(True)
sleep(1)

display.invert(False)
sleep(1)

display.clear() # Black
