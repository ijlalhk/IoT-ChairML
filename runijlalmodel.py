from machine import ADC, Pin
import time
from ultrasonic import HCSR04
from ijlalmodel import RandomForestClassifier

# Define the analog pin for the flex sensor
flex_pin = ADC(Pin(26))

# Initialize the ultrasonic sensors
ultrasonic_sensor1 = HCSR04(trigger_pin=15, echo_pin=16)
ultrasonic_sensor2 = HCSR04(trigger_pin=19, echo_pin=18)

# Initialize the classifier
clf = RandomForestClassifier()

# Mapping of numeric predictions to posture names
posture_map = {
    0: "Good",
    1: "LeanForward",
    2: "LeanBackward",
    3: "Not Properly On Seat"
}

def average_window(window):
    return sum(window) / len(window) if window else 0

while True:
    # Collect samples every 0.1 seconds
    flex_samples, distance1_samples, distance2_samples = [], [], []
    
    for _ in range(10):
        flex_samples.append(abs(flex_pin.read_u16()))
        distance1_samples.append(abs(ultrasonic_sensor1.distance_cm()))
        distance2_samples.append(abs(ultrasonic_sensor2.distance_cm()))
        time.sleep(0.1)

    # Calculate averages of the samples
    avg_flex = average_window(flex_samples)
    avg_distance1 = average_window(distance1_samples)
    avg_distance2 = average_window(distance2_samples)
    avg_of_yz = average_window([avg_distance1, avg_distance2])

    # Prepare the input features
    input_features = [avg_flex, avg_of_yz]  # Ensure it's a list of lists
    
    # Predict posture using the trained model
    try:
        prediction = clf.predict(input_features)  # Pass input_features as a list of lists
        current_posture = posture_map.get(prediction, "Unknown")  # Map the prediction to the posture name
    except Exception as e:
        print("Error during prediction:", e)
        current_posture = "Unknown"

    # Print sensor values with labels
    print(f"Flex: {avg_flex:.2f}, AvgYZ: {avg_of_yz:.2f}, Posture: {current_posture}")
    
    # Wait for 1 second before the next set of readings
    time.sleep(1)
