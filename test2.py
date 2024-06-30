from machine import ADC, Pin
import time
from ultrasonic import HCSR04  # Import the ultrasonic sensor module

# Define the analog pin for the flex sensor
flex_pin = ADC(Pin(26))  # A0 is GPIO 26 on Nano RP2040

# Initialize the ultrasonic sensors
ultrasonic_sensor1 = HCSR04(trigger_pin=15, echo_pin=16)
ultrasonic_sensor2 = HCSR04(trigger_pin=19, echo_pin=18)

# Initialize the posture variable
previous_posture = "Good"
current_posture= 'Good'

while True:
    flex_value = flex_pin.read_u16()  # Read the analog value from the flex sensor
    distance1 = ultrasonic_sensor1.distance_cm()  # Read the distance from the first ultrasonic sensor
    distance2 = ultrasonic_sensor2.distance_cm()  # Read the distance from the second ultrasonic sensor
    # Round the distances to two decimal places
    distance1 = round(distance1, 2)
    distance2 = round(distance2, 2)
    # Determine posture based on sensor readings
    if distance1 == -0.02 or distance2 == -0.02:
        print("FAULTY SENSOR")
    else:
        print("GOOD SENSOR")
        if flex_value > 4000:
            if distance1 < 11 and distance2 < 10:
                current_posture = "Good"
            else:
                current_posture = "Bad"
        else:
            current_posture = "Bad"
        previous_posture = current_posture
    
    # Format the data with labels as a comma-separated string
    data = "Flex: {}, Ultrasonic1: {:.2f} cm, Ultrasonic2: {:.2f} cm, Posture: {}".format(flex_value, distance1, distance2, current_posture)
    
    # Print the sensor values with labels
    print(data)
    
    # Wait for 500 milliseconds before the next reading
    time.sleep(0.5)
