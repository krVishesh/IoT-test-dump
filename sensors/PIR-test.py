from machine import Pin
import time

# Define PIR sensor pin and LED pin
PIR_PIN = 2
LED_PIN = 15
LED_PIN2 = 21

# Initialize PIR sensor and LED
pir = Pin(PIR_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)
led2 = Pin(LED_PIN2, Pin.OUT)

print("PIR Sensor Test - Waiting for motion...")

while True:
    if pir.value() == 1:
        print("Motion detected!")
        led.value(1)  # Turn on LED
        led2.value(1)  # Turn on LED
        time.sleep(2)  # Delay to avoid multiple triggers
    else:
        led.value(0)  # Turn off LED
        led2.value(0)  # Turn off LED
    
    time.sleep(0.1)
