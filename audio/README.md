# Audio Tests

This directory contains MicroPython test scripts for audio-related components and functionality, designed for ESP32 microcontrollers.

## Development Environment

- **IDE**: Thonny IDE
- **Language**: MicroPython
- **Target Hardware**: ESP32 microcontrollers
- **Purpose**: Test scripts for verifying audio component functionality

## Available Tests

- `Speaker-Test.py` - Test for speaker output
- `INMP441-16bit-Test.py` - Test for INMP441 microphone (16-bit mode)
- `INMP441-24bit-Test.py` - Test for INMP441 microphone (24-bit mode)

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

Make sure to connect the appropriate audio components before running the tests. 