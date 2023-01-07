# Led
# Turns on an external LED for one second, then off for one second, repeatedly
# The external LED shall be connected to pin GP15 through a 330 ohms resistor.
# The resistor limits the amount of current the LED can draw.
# Without it, the LED can draw too much current and burn itself

import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.value(True)
    utime.sleep(1)
    led.value(False)
    utime.sleep(1)
