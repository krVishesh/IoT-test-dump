# Sensor Tests

This directory contains MicroPython test scripts for various sensors used in IoT projects with ESP32 microcontrollers.

## Development Environment

- **IDE**: Thonny IDE
- **Language**: MicroPython
- **Target Hardware**: ESP32 microcontrollers
- **Purpose**: Test scripts for verifying sensor functionality and integration

## Available Tests

- `BMP280-test.py` - Test for BMP280 temperature and pressure sensor
- `DHT11-Test.py` - Test for DHT11 temperature and humidity sensor
- `Flame-Test.py` - Test for flame detection sensor
- `Heartrate-test.py` - Test for heart rate sensor
- `INMP441-Test.py` - Test for INMP441 microphone sensor (various bit depths)
- `PIR-test.py` - Test for PIR motion sensor
- `Ultrasonic-test.py` - Test for ultrasonic distance sensor

## Requirements

- Thonny IDE with MicroPython support
- ESP32 microcontroller with MicroPython firmware
- Required MicroPython packages (machine, time, etc.)
- Specific hardware components as listed in each test file

## Usage

1. Open the desired test script in Thonny IDE
2. Connect your ESP32 to the computer
3. Select the ESP32 as the interpreter in Thonny
4. Run the script using the Run button in Thonny

Make sure to connect the appropriate hardware components before running the tests. 