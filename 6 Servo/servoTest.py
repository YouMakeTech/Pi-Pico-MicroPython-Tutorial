# servoTest.py
# Move a servo motor
#
# Connect the servo orange wire (=signal) to pin GP15
# the servo red wire (=+5V) to pin VBUS
# and the servo brown wire (=GND) to pin GND

import machine
import utime

pwm = machine.PWM(machine.Pin(15))
pwm.freq(50) # 50 Hz = 20 ms period

while True:
    pwm.duty_ns(1500000) # Servo center = 1.5 ms pulsewidth
    utime.sleep(1)       # Pause 1 second
    pwm.duty_ns(600000)  # Servo min. angle = 0.6 ms pulsewidth
    utime.sleep(1)       # Pause 1 second
    pwm.duty_ns(2400000)  # Servo max. angle = 2.4 ms pulsewidth
    utime.sleep(1)       # Pause 1 second
    pwm.duty_ns(1500000) # Servo center = 1.5 ms pulsewidth
    utime.sleep(5)       # Pause 5 seconds
