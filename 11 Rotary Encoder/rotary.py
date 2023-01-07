# A simplified MicroPython driver to read a rotary encoder
# based on Ben Buxton's and Mike Teachman's implementation
# http://www.buxtronix.net/2011/10/rotary-encoders-done-properly.html
# https://github.com/buxtronix/arduino/tree/master/libraries/Rotary
# https://github.com/miketeachman/micropython-rotary
#
# Usage:
# * Connect a rotary encoder to GPIO Pins 16 and 17. Connect the GND
# * Copy rotary.py to the root directory of the Raspberry Pi Pico
# * In the MicroPython shell type:
# >>> from rotary import Rotary
# >>> r = Rotary(16,17)
# * Turn left and right

from machine import Pin

class Rotary:

    def __init__(self, pin1id, pin2id):
        self.pin1 = Pin(pin1id, Pin.IN, Pin.PULL_UP)
        self.pin2 = Pin(pin2id, Pin.IN, Pin.PULL_UP)
        self.currentValue = 0
        self.angle = 0
        self.onPinValueChange(self.pin1)

        self.pin1.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = self.onPinValueChange)
        self.pin2.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = self.onPinValueChange)
        
    def onPinValueChange(self, pin):
        previousValue = self.currentValue
        self.currentValue = (self.pin1.value() << 1) | self.pin2.value()
        
        if self.currentValue != previousValue:
#             print(str(int(self.currentValue&2>0)) + str(int(self.currentValue&1>0)))
            
            transition = previousValue<<2 | self.currentValue
            if transition in [0b1101, 0b0100, 0b0010, 0b1011]:
                # Clockwise transition
                self.angle += 1
            elif transition in [0b1110, 0b1000, 0b0001, 0b0111]:
                # Counter-Clockwise transition
                self.angle -= 1
#             print(str(self.angle))

    def get(self):
        return self.angle
        