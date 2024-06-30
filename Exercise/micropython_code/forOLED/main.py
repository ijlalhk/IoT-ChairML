from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# Initialize I2C interface with the correct pins for your setup
i2c = SoftI2C(scl=Pin(13), sda=Pin(12))

# Initialize SSD1306 OLED display
oled_width = 128
oled_height = 32  # Adjusted for 128x32 OLED display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Clear the display
    oled.fill(0)
    
    # Display some text
    oled.text('Hello, World 1!', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Hello, World 3!', 0, 20)
    
    # Update the display
    oled.show()
    
    # Wait for a bit before updating again
    sleep(1)

