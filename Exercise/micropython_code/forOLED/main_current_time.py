from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import utime

# Initialize I2C interface with the correct pins for your setup
i2c = SoftI2C(scl=Pin(13), sda=Pin(12))

# Initialize SSD1306 OLED display
oled_width = 128
oled_height = 32  # Adjusted for 128x32 OLED display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Clear the display
    oled.fill(0)
    
    # Get the current time
    current_time = utime.localtime()
    time_str = '{:02}:{:02}:{:02}'.format(current_time[3], current_time[4], current_time[5])
    
    # Display the current time
    oled.text('Current Time:', 0, 0)
    oled.text(time_str, 0, 10)
    
    # Update the display
    oled.show()
    
    # Wait for a bit before updating again
    sleep(1)

