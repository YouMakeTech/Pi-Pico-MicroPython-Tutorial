# Servo.py
# simple class to move a servo motor
#
# from Servo import Servo
# servo15 = Servo(15) # connect servo to pin GP15
# servo15.move(0)
# servo15.move(-90)
# servo15.move(90)

import machine

class Servo:
   
    def __init__(self, pin):
        self.pin = pin
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(50) # 50 Hz = 20 ms period
        self.pwm.duty_ns(1500000) # center servo
        
    def write(self, angle):
        self.pwm.duty_ns(self.angleToPulse(angle))
        
    def angleToPulse(self,angle):
        # pulse = angleToPulse()
        # convert a servo angle to a pulse width
        # angle is a float between -90 degrees and +90 degrees
        # pulse is the pulse width in ns to send to the servo
    
        MIN_ANGLE = -90.0
        MAX_ANGLE =  90.0
        MIN_PULSE =  600000 # pulse width for MIN_ANGLE in ns 
        MAX_PULSE = 2400000 # pulse width for MAX_ANGLE in ns for MIN_ANGLE
    
        # Force input angle to be within -90 and +90 degrees
        angle = min(angle, MAX_ANGLE) 
        angle = max(angle, MIN_ANGLE)
    
        pulse = MIN_PULSE + (angle - MIN_ANGLE) * (MAX_PULSE - MIN_PULSE)/(MAX_ANGLE - MIN_ANGLE)
        return int(pulse)
        