from st7789 import ST7789
from time import sleep

display = ST7789()
# display = ST7789(width, height, sck=18, mosi=19, dc=20, rst=21, cs=17, bl=22, baudrate=62500000)

while True:
    display.fill(0)
    display.line(0, 0, 239, 239, ST7789.color(255, 255, 0))
    display.show()
    sleep(0.01)
    
    display.fill(ST7789.color(255, 0, 0))
    display.line(0, 0, 239, 239, ST7789.color(255, 255, 0))
    display.show()
    sleep(0.01)
    
    display.fill(ST7789.color(0, 255, 0))
    display.line(0, 0, 239, 239, ST7789.color(255, 255, 0))
    display.show()
    sleep(0.01)
    
    display.fill(ST7789.color(0, 255, 0))
    display.line(0, 0, 239, 239, ST7789.color(255, 255, 0))
    display.show()
    sleep(0.01)
