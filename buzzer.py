from machine import Pin
from time import sleep_us, ticks_us, ticks_diff

def buzz_for_one_second():
    buzzer = Pin(20, Pin.OUT)
    # get the current time in microseconds
    start_time = ticks_us()

    # generate a 500Hz on/off signal for 1 second
    while ticks_diff(ticks_us(), start_time) < 1_000_000:  # 1 second = 1,000,000 microseconds
        # this switches on for 1ms = 1000 us
        buzzer.on()
        sleep_us(1000)
        # this switches off for 1 ms = 1000 us
        buzzer.off()
        sleep_us(1000)

# Usage:
# Call the function with the appropriate pin number
#buzz_for_one_second()
