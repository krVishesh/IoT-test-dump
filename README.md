# IoT Test Suite

This repository contains a collection of MicroPython test scripts for various IoT components and sensors, specifically designed for ESP32 microcontrollers. The tests are organized into different categories based on their functionality.

## Development Environment

- **IDE**: Thonny IDE
- **Language**: MicroPython
- **Target Hardware**: ESP32 microcontrollers (various variants)
- **Purpose**: Test scripts for verifying hardware functionality and component integration

## Directory Structure

- `sensors/` - Tests for various sensors (temperature, humidity, motion, etc.)
- `actuators/` - Tests for motors, servos, and other actuating devices
- `communication/` - Tests for wireless communication protocols (WiFi, ESP-Now)
- `storage/` - Tests for SD card and file operations
- `input-devices/` - Tests for buttons, joysticks, and other input devices
- `audio/` - Tests for audio-related components

## Requirements

- Thonny IDE
- MicroPython firmware for ESP32
- Various hardware components as specified in each test file
- Required MicroPython packages (listed in individual README files)

## Usage

Each directory contains its own README file with specific instructions for the tests in that category. Refer to the individual README files for detailed information about setup and usage.

## Contributing

Feel free to contribute new test scripts or improve existing ones. Please follow the existing directory structure and documentation format.