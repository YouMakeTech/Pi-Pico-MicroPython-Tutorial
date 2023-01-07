from machine import Pin, PWM
import time

# Passive piezo buzzer connected to pin GP18
buzzer = PWM(Pin(18))

# Play an A5 note (=440 Hz) for one second
buzzer.duty_u16(16384) # 16384 = 25% duty cycle
buzzer.freq(440)       # A5 = 440 Hz
time.sleep(1)
buzzer.duty_u16(0)

time.sleep(2)          # pause 2 seconds

# play a "blip" sound
buzzer.freq(1000)      # 1000 Hz
buzzer.duty_u16(16384) # 16384 = 25% duty cycle
time.sleep(0.050)
buzzer.duty_u16(0)     # stop the sound (= 0% duty cycle)

time.sleep(2)          # pause 2 seconds

