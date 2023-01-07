# BreathingLED.py
# The Raspberry Pi Pico has no analog output.
# There is a way to fake an analog output using PWM (Pulse Width Modulation)
# Connect a LED to GP15. Do not forget to add a 330 ohms resistor in serie

import machine
import utime

pwm = machine.PWM(machine.Pin(15))
pwm.freq(1000) # Hz


while True:
    for dutyCyclePercent in range(0,100):
        print("Setting the PWM to " + str(dutyCyclePercent) + "%")
        pwm.duty_u16(int((dutyCyclePercent*65535.)/100.))
        utime.sleep(0.020) # sleep in seconds
    
    for dutyCyclePercent in range(100,0,-1):
        print("Setting the PWM to " + str(dutyCyclePercent) + "%")
        pwm.duty_u16(int((dutyCyclePercent*65535.)/100.))
        utime.sleep(0.020) # sleep in seconds
 