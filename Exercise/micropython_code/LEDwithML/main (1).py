import my_model
import time
from lsm6dsox import LSM6DSOX
from machine import Pin, I2C, SoftI2C
import ssd1306

# RGB LED connected to the RP2040
ledG = Pin(25, Pin.OUT)
ledR = Pin(15, Pin.OUT)
ledB = Pin(16, Pin.OUT)
ledR.on()
ledB.on()
ledG.on()

# Initialize I2C interface for OLED
i2c = SoftI2C(scl=Pin(13), sda=Pin(12))

# Initialize SSD1306 OLED display
oled_width = 128
oled_height = 32  # Adjusted for 128x32 OLED display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Scan for I2C devices
devices = i2c.scan()
if not devices:
    raise RuntimeError('No I2C devices found')
else:
    print('I2C devices found:', devices)

# Initialize the LSM6DSOX sensor
lsm = LSM6DSOX(i2c)
clf = my_model.RandomForestClassifier()

# Function to calculate the delta value
def calculate_delta(prev, curr):
    return [curr[i] - prev[i] for i in range(3)]

# Function to classify the device state
def classify_state(accel_data, delta):
    combined_data = list(accel_data) + delta  # Ensure both are lists before concatenating
    a = clf.predict(combined_data)
    return a

# Function to update the OLED display based on the state
def update_display(state):
    oled.fill(0)  # Clear the display
    if state == 0:
        oled.text('On table', 0, 0)
    elif state == 1:
        oled.text('In hand', 0, 0)
    elif state == 2:
        oled.text('Rotating', 0, 0)
    oled.show()  # Update the display

# Initialize previous data with the first reading
prev_data = lsm.accel()

# Run the loop
while True:
    # Get current accelerometer data
    curr_data = lsm.accel()
    
    # Calculate delta values
    delta = calculate_delta(prev_data, curr_data)
    
    # Classify the state of the device
    state = classify_state(list(curr_data), delta)
    print(state)
    
    # Update the OLED display based on the classified state
    update_display(state)
    
    # Update previous data
    prev_data = curr_data
    
    # Wait for 100 ms
    time.sleep_ms(100)
