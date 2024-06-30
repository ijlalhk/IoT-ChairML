from machine import ADC, Pin
import time
from ultrasonic import HCSR04  # Import the ultrasonic sensor module

# Define the analog pin for the flex sensor
flex_pin = ADC(Pin(26))  # A0 is GPIO 26 on Nano RP2040

# Initialize the ultrasonic sensors
ultrasonic_sensor1 = HCSR04(trigger_pin=15, echo_pin=16)
ultrasonic_sensor2 = HCSR04(trigger_pin=19, echo_pin=18)

while True:
    flex_value = flex_pin.read_u16()  # Read the analog value from the flex sensor
    distance1 = ultrasonic_sensor1.distance_cm()  # Read the distance from the first ultrasonic sensor
    distance2 = ultrasonic_sensor2.distance_cm()  # Read the distance from the second ultrasonic sensor
    
    # Determine posture based on sensor readings
    if distance1 < 10 and distance2 < 10 and flex_value > 4000:
        posture = "Good"
    else:
        posture = "Bad"
    
    # Format the data with labels as a comma-separated string
    data = "Flex: {}, Ultrasonic1: {:.2f} cm, Ultrasonic2: {:.2f} cm, Posture: {}".format(flex_value, distance1, distance2, posture)
    
    # Print the sensor values with labels
    print(data)
    
    # Wait for 500 milliseconds before the next reading
    time.sleep(0.5)
