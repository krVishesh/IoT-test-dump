# Actuator Tests

This directory contains MicroPython test scripts for various actuators and motor control components, designed for ESP32 microcontrollers.

## Development Environment

- **IDE**: Thonny IDE
- **Language**: MicroPython
- **Target Hardware**: ESP32 microcontrollers
- **Purpose**: Test scripts for verifying actuator and motor control functionality

## Available Tests

- `Car-test.py` - Test for car/motor control system
- `DRV-test.py` - Test for DRV motor driver
- `Motor-test.py` - Test for basic motor control
- `PWM-test.py` - Test for PWM (Pulse Width Modulation) control
- `Servo-test.py` - Test for servo motor control
- `Neopixel-Test.py` - Test for Neopixel LED strip control
- `LED-test.py` - Test for basic LED control
- `Board-LED.py` - Test for board-mounted LED control

## Requirements

- Thonny IDE with MicroPython support
- ESP32 microcontroller with MicroPython firmware
- Required MicroPython packages (machine, time, neopixel, etc.)
- Specific hardware components as listed in each test file

## Usage

1. Open the desired test script in Thonny IDE
2. Connect your ESP32 to the computer
3. Select the ESP32 as the interpreter in Thonny
4. Run the script using the Run button in Thonny

Make sure to connect the appropriate hardware components before running the tests. 