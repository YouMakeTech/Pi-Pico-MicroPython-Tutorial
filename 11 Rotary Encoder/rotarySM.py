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
# >>> r = RotarySM(16,17)
# * Turn left and right

from micropython import const
from machine import Pin

DIR_CW = const(0x10)  # Clockwise step
DIR_CCW = const(0x20)  # Counter-clockwise step

# Rotary Encoder States
R_START = const(0x0)
R_CW_1 = const(0x1)
R_CW_2 = const(0x2)
R_CW_3 = const(0x3)
R_CCW_1 = const(0x4)
R_CCW_2 = const(0x5)
R_CCW_3 = const(0x6)
R_ILLEGAL = const(0x7)

TRANSITION_TABLE = [

    # |------------- NEXT STATE -------------|            |CURRENT STATE|
    # CLK/DT    CLK/DT     CLK/DT    CLK/DT
    #   00        01         10        11
    [R_START, R_CCW_1, R_CW_1,  R_START],             # R_START
    [R_CW_2,  R_START, R_CW_1,  R_START],             # R_CW_1
    [R_CW_2,  R_CW_3,  R_CW_1,  R_START],             # R_CW_2
    [R_CW_2,  R_CW_3,  R_START, R_START | DIR_CW],   # R_CW_3
    [R_CCW_2, R_CCW_1, R_START, R_START],             # R_CCW_1
    [R_CCW_2, R_CCW_1, R_CCW_3, R_START],             # R_CCW_2
    [R_CCW_2, R_START, R_CCW_3, R_START | DIR_CCW],  # R_CCW_3
    [R_START, R_START, R_START, R_START]]             # R_ILLEGAL

STATE_MASK = const(0x07)
DIR_MASK = const(0x30)

class RotarySM:

    def __init__(self, pin1id, pin2id):
        self.pin1 = Pin(pin1id, Pin.IN, Pin.PULL_UP)
        self.pin2 = Pin(pin2id, Pin.IN, Pin.PULL_UP)
        self.currentValue = 0
        self.state = R_START
        self.onPinValueChange(self.pin1)

        self.pin1.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = self.onPinValueChange)
        self.pin2.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = self.onPinValueChange)
        
    def onPinValueChange(self, pin):
        previousValue = self.currentValue
        self.currentValue = (self.pin1.value() << 1) | self.pin2.value()
        
        if self.currentValue != previousValue:
            print(str(int(self.currentValue&2>0)) + str(int(self.currentValue&1>0)))

            # Determine next state
            self.state = TRANSITION_TABLE[self.state & STATE_MASK][self.currentValue]
            
#             print(self.getStateStr())
            print(self.getDirectionStr())
        
    def getStateStr(self):
        s="?????"
        state = self.state & STATE_MASK
        if state == R_START:
            s="R_START"
        elif state == R_CW_1:
            s="R_CW_1"
        elif state == R_CW_2:
            s="R_CW_2"
        elif state == R_CW_3:
            s="R_CW_3"
        elif state == R_CCW_1:
            s="R_CCW_1"
        elif state == R_CCW_2:
            s="R_CCW_2"
        elif state == R_CCW_3:
            s="R_CCW_3"
        elif state == R_ILLEGAL:
            s="R_ILLEGAL"
        return(s)
    
    def getDirectionStr(self):
        direction = self.state & DIR_MASK
        if direction == DIR_CW:
            s = "DIR_CW"
        elif direction == DIR_CCW:
            s = "DIR_CCW"
        else:
            s = ""
        return(s)
        
