# README

## Project: IoT ChairML

This project uses IoT and machine learning to monitor and improve posture through an IoT-enabled chair. It involves data collection, machine learning models, and various sensor integrations.

### Contents

- **Exercise/**
  - **Jupyter Notebook/**
    - `Classifier.ipynb`: Notebook for training and evaluating the posture classification model.
    - `MyModel.py`: Python file containing the machine learning model implementation.
    - `Untitled.ipynb`: Additional notebook (unnamed) for exploratory analysis or experimentation.
    - `Untitled1.ipynb`: Another additional notebook (unnamed) for exploratory analysis or experimentation.
    - **aaa/**
      - `in_hand.csv`: Data collected while the device was held in hand.
      - `input_data.csv`: Initial input data for training.
      - `newdata1.csv`: Updated dataset.
      - `notmoving.csv`: Data collected while the device was stationary.
      - `rotating.csv`: Data collected while the device was rotating.
      - `t_data - Copy.csv`: Copy of training data.
      - `t_data.csv`: Training data.
    - `datafinal - Copy.csv`: Copy of the final dataset used.
    - `datafinal.csv`: Final dataset used for training and evaluation.
    - **newData/**
      - `1newdata.csv`: Newly collected data.
      - `inhand.txt`: Notes or data from the in-hand position.
      - `left right.txt`: Notes or data from left-right movement.
      - `newdata.csv`: Newly collected dataset.
      - `newdata.xlsx`: Excel file of newly collected data.
      - `ontable.txt`: Notes or data from the on-table position.
    - `updated_labels.csv`: Updated labels for the datasets.
  - **micropython_code/**
    - `LEDTask2.txt`: Task 2 instructions for LED control.
    - **LEDwithML/**
      - `main (1).py`: Main script for LED control with ML.
      - `my_model.py`: Model script for LED control.
      - `ssd1306 (2).py`: Script for SSD1306 OLED display control.
    - **collectData/**
      - `collectdataandsaveitMAIN.py`: Script for collecting and saving sensor data.
    - **flexsensor/**
      - `reafFlexandSave.py`: Script for reading flex sensor data and saving it.
    - **forOLED/**
      - `main.py`: Main script for OLED display control.
      - `main_current_time.py`: Script for displaying current time on OLED.
      - `screen.py`: Helper script for OLED display control.
      - `ssd1306.py`: Script for SSD1306 OLED display control.
    - `led and sound.txt`: Instructions for LED and sound integration.
    - `ledandsensorsRULEBASED.txt`: Rule-based integration of LED and sensors.
    - `ontableNotMoved.txt`: Data or notes when the device was on a table and not moved.
    - `rotating.txt`: Data or notes from rotating movement.
    - `rulebasedhandorstill.txt`: Rule-based data for hand-held or still positions.
    - `task 2.2.txt`: Task 2.2 instructions.
    - `task1 LED.txt`: Task 1 instructions for LED control.
    - `task6.1.txt`: Task 6.1 instructions.
- **ExplanationVideo.mp4**: [Video explanation of the project](ExplanationVideo.mp4)
- **MyModel.py**: Python script for the main machine learning model.
- **Posture Promo.mp4**: [Promotional video for the posture monitoring system](Posture Promo.mp4)
- **Posture.py**: Python script for posture-related functions.
- **Presentation.pptx**: [Project presentation slides](Presentation.pptx)
- **Schematic Diagram.drawio.pdf**: [Schematic diagram of the system](Schematic Diagram.drawio.pdf)
- **altrasonictest.py**: Script for testing ultrasonic sensor.
- **buzzer.py**: Script for controlling a buzzer.
- **flex_sensor_data.txt**: Data from the flex sensor.
- **ijlalmodel.py**: Alternative model implementation.
- **main.py**: Main script for running the system.
- **run_model.py**: Script for running the machine learning model.
- **runijlalmodel.py**: Script for running the alternative model.
- **screen.py**: Script for OLED screen control.
- **ssd1306.py**: Script for SSD1306 OLED display control.
- **test.py**: Test script for various functionalities.
- **test2.py**: Additional test script.
- **ultrasonic.py**: Script for controlling the ultrasonic sensor.

### Setup and Usage

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ijlalhk/IoT-ChairML.git
   cd IoT-ChairML
