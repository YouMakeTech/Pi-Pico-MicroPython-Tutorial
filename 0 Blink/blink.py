import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.value(True)
    utime.sleep(1)
    led.value(False)
    utime.sleep(1)
    
