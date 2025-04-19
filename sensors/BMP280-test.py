from machine import Pin, I2C
import time
from bmp280 import BME280

# Initialize I2C with custom pins for ESP32-C6
i2c = I2C(0, scl=Pin(19), sda=Pin(20), freq=100000)

# Initialize BMP280/BME280 Sensor
sensor = BME280(i2c=i2c)

while True:
    print(f"Temperature: {sensor.temperature}")
    print(f"Pressure: {sensor.pressure}")
    print(f"Humidity: {sensor.humidity}")  # Only valid for BME280
    print("---------------------")
    time.sleep(2)
