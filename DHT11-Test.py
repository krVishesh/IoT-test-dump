import dht
from machine import Pin
import time

# Initialize DHT11 on GPIO 18
dht_sensor = dht.DHT11(Pin(27))

while True:
    try:
        dht_sensor.measure()  # Read sensor data
        temperature = dht_sensor.temperature()  # Get temperature (°C)
        humidity = dht_sensor.humidity()  # Get humidity (%)

        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

    except OSError as e:
        print("Failed to read sensor:", e)

    time.sleep(2)  # Wait before next reading
