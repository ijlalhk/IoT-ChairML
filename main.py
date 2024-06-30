from machine import ADC, Pin
import time
import screen  # Import the screen module
from ultrasonic import HCSR04  # Import the ultrasonic sensor module

# Define the analog pin for the flex sensor
flex_pin = ADC(Pin(26))  # A0 is GPIO 26 on Nano RP2040

# Define the digital pin for the push button
button_pin = Pin(25, Pin.IN, Pin.PULL_UP)  # D2 is GPIO 25 on Nano RP2040

# Initialize the ultrasonic sensors
ultrasonic_sensor1 = HCSR04(trigger_pin=15, echo_pin=16)
ultrasonic_sensor2 = HCSR04(trigger_pin=19, echo_pin=18)

# Variable to track the recording state
recording = False

# Function to record data
def record_data():
    # Open a file in append mode
    with open("/flex_sensor_data.txt", "w") as file:
        for i in range(300):
            flex_value = flex_pin.read_u16()  # Read the analog value from the flex sensor
            distance1 = ultrasonic_sensor1.distance_cm()  # Read the distance from the first ultrasonic sensor
            distance2 = ultrasonic_sensor2.distance_cm()  # Read the distance from the second ultrasonic sensor
            data = "{},{:.2f},{:.2f},3".format(flex_value, distance1, distance2)
            
            # Print the sensor values
            print(data)
            
            # Write the data to the file
            file.write(data + "\n")
            
            # Update the OLED display with the sensor values
            screen.update_display("Flex: {}".format(flex_value), "Dist1: {:.2f} cm".format(distance1), "Dist2: {:.2f} cm".format(distance2))
            
            time.sleep(0.5)  # Wait for 500 milliseconds before the next reading

# Function to count the lines in the file
def count_lines(filename):
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file)
    except OSError:
        return 0

# Check the number of rows at the start
num_rows = count_lines("/flex_sensor_data.txt")
screen.update_display("Startup", "System ready", "Rows: {}".format(num_rows))

while True:
    # Check if the button is pressed
    if not button_pin.value():
        # Debounce the button press
        time.sleep(0.1)
        if not button_pin.value():
            # Toggle the recording state
            recording = not recording
            
            # If recording, start recording data
            if recording:
                screen.update_display("Recording started", "", "")
                record_data()
                screen.update_display("Recording stopped", "", "Rows: {}".format(count_lines("/flex_sensor_data.txt")))
            else:
                # Display the number of rows in the text file when stopped
                num_rows = count_lines("/flex_sensor_data.txt")
                screen.update_display("Recording stopped", "", "Rows: {}".format(num_rows))
        
        # Wait for the button to be released
        while not button_pin.value():
            time.sleep(0.1)
    
    # Short delay to avoid busy-waiting
    time.sleep(0.1)