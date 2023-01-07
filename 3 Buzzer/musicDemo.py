# musicDemo.py by YouMakeTech
# play Super Mario Bros Theme on a piezzo buzzer
# by changing the PWM frequency
#
# Connect a passive buzzer to pin GP18

# Note frequencies in Hz (A4 = 440 Hz)
SILENCE = 0
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 689
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988
NOTE_C6 = 1047

# Note lengths in seconds
WHOLE = 0.4
HALF = WHOLE/2.
QUARTER = WHOLE/4.
EIGHTH = WHOLE/8.

# Super Mario Bros Theme 
note = [NOTE_E5, NOTE_E5, SILENCE, NOTE_E5, SILENCE, NOTE_C5, NOTE_E5, SILENCE, NOTE_G5]
noteLength = [EIGHTH, EIGHTH, EIGHTH, EIGHTH, EIGHTH, EIGHTH, QUARTER, EIGHTH, HALF]

from machine import Pin, PWM
import time

buzzer = PWM(Pin(18))

buzzer.duty_u16(0) # no sound

while True:
    for i in range(0,len(note)):
        if note[i]>0:
            buzzer.freq(note[i])
            buzzer.duty_u16(16384) # 25% duty cycle
        else:
            buzzer.duty_u16(0) # 0% duty cycle => no sound
        
        time.sleep(noteLength[i])
        buzzer.duty_u16(0) # 0% duty cycle => no sound
        time.sleep(QUARTER)
       
    time.sleep(2) # replay music after a pause of 2 seconds
        
    