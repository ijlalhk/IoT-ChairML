from machine import ADC, Pin
import time
from ultrasonic import HCSR04
from Posture import RandomForestClassifier
from buzzer import buzz_for_one_second

# Define the analog pin for the flex sensor
flex_pin = ADC(Pin(26))

# Initialize the ultrasonic sensors
ultrasonic_sensor1 = HCSR04(trigger_pin=15, echo_pin=16)
ultrasonic_sensor2 = HCSR04(trigger_pin=19, echo_pin=18)

# Initialize the classifier
clf = RandomForestClassifier()

# Mapping of numeric predictions to posture names
posture_map = {
    0: "Good Posture",
    1: "Leaning Forward",
    2: "Leaning Backward",
    3: "Not Properly On Seat"
}

# Initialize lists for sliding window of sensor readings (10 seconds with 1-second interval = 10 samples)
window_size = 10
flex_window, distance1_window, distance2_window = [], [], []

def average_window(window):
    return sum(window) / len(window) if window else 0

while True:
    # Collect samples every 0.1 seconds
    flex_samples, distance1_samples, distance2_samples = [], [], []
    
    # Read sensor values
    sensor1_value = abs(ultrasonic_sensor1.distance_cm())
    sensor2_value = abs(ultrasonic_sensor2.distance_cm())
    flex_sensor_value = abs(flex_pin.read_u16())

    # Compute delta
    delta = sensor1_value - sensor2_value

    # Prepare the input for the model
    input_features = (flex_sensor_value, delta)
    
    # Predict using the custom RandomForest model
    prediction = clf.predict(input_features)  # Ensure that your Posture.py has a 'predict' method that accepts the proper format
    current_posture = posture_map.get(prediction, "Unknown")
    # Output the prediction result
    print(f"Flex: {flex_sensor_value:.2f}, Upper: {sensor1_value:.2f} cm, Lower: {sensor2_value:.2f} cm, Delta: {delta:.2f}, Posture: {current_posture}")
#     
    print("Predicted Category:", prediction)
    if prediction != 0:
        buzz_for_one_second()
    
    time.sleep(3)
    
#     for _ in range(10):
#         # Read sensor values
#         flex_samples.append(flex_pin.read_u16())
#         distance1_samples.append(ultrasonic_sensor1.distance_cm())
#         distance2_samples.append(ultrasonic_sensor2.distance_cm())
#         time.sleep(0.1)
#     
#     # Calculate averages of the samples
#     avg_flex = average_window(flex_samples)
#     avg_distance1 = average_window(distance1_samples)
#     avg_distance2 = average_window(distance2_samples)
#     
#     # Add averages to the sliding window
#     flex_window.append(avg_flex)
#     distance1_window.append(avg_distance1)
#     distance2_window.append(avg_distance2)
#     
#     # Maintain sliding window size
#     if len(flex_window) > window_size:
#         flex_window.pop(0)
#     if len(distance1_window) > window_size:
#         distance1_window.pop(0)
#     if len(distance2_window) > window_size:
#         distance2_window.pop(0)
#     
#     # Prepare current readings as input features
#     avg_flex_window = average_window(flex_window)
#     avg_distance1_window = average_window(distance1_window)
#     avg_distance2_window = average_window(distance2_window)
#     
#     # Derive additional features (velocities)
#     vel_flex = flex_window[-1] - flex_window[-2] if len(flex_window) > 1 else 0
#     vel_distance1 = distance1_window[-1] - distance1_window[-2] if len(distance1_window) > 1 else 0
#     vel_distance2 = distance2_window[-1] - distance2_window[-2] if len(distance2_window) > 1 else 0
#     
#     # Ensure all 6 features are included
#     input_features = [avg_flex_window, avg_distance1_window, avg_distance2_window, vel_flex, vel_distance1, vel_distance2]
#     
#     # Debugging information
#     print("Input features:", input_features)
#     
#     # Validate input features length (should be the expected feature length)
#     expected_length = 6  # Update this based on your actual model's expected input length
#     if len(input_features) != expected_length:
#         print(f"Error: Expected input features length {expected_length}, but got {len(input_features)}")
#         continue
#     
#     # Predict posture using the trained model
#     try:
#         prediction = clf.predict(input_features)  # Pass input_features as a list of lists
#         print("Prediction result:", prediction)  # Debugging information
#         current_posture = posture_map.get(prediction, "Unknown")  # Map the prediction to the posture name
#     except Exception as e:
#         print("Error during prediction:", e)
#         current_posture = "Unknown"
# 
#     # Print sensor values with labels
#     print(f"Flex: {avg_flex_window:.2f}, Ultrasonic1: {avg_distance1_window:.2f} cm, Ultrasonic2: {avg_distance2_window:.2f} cm, Posture: {current_posture}")
#     
    # Wait for 1 second before the next set of readings
    #time.sleep(1)
