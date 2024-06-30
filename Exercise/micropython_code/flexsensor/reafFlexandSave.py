from machine import ADC, Pin
import time
import screen  # Import the screen module

# Define the analog pin
flex_pin = ADC(Pin(26))  # A0 is GPIO 26 on Nano RP2040

# Open a file in write mode
with open("/flex_sensor_data.txt", "w") as file:
    for i in range(100):
        flex_value = flex_pin.read_u16()  # Read the analog value from the flex sensor
        voltage = flex_value * (3.3 / 65535)  # Convert the value to voltage (0-3.3V)
        data = "Flex Sensor Value: {}, Voltage: {:.2f} V".format(flex_value, voltage)
        
        # Print the sensor value and voltage
        print(data)
        
        # Write the data to the file
        file.write(data + "\n")
        
        # Update the OLED display with the sensor values
        screen.update_display("Flex Value: {}".format(flex_value), "Voltage: {:.2f} V".format(voltage), "Reading: {}".format(i+1))
        
        time.sleep(0.5)  # Wait for 500 milliseconds before the next reading

