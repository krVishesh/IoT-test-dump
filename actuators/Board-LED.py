from machine import Pin
import neopixel
import time

NEOPIXEL_PIN = 21  # NeoPixel Pin 21 for ESP32-S3, 8 for ESP32-C6

np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), 1)

def light_up(color):
    np[0] = color
    np.write()

while True:
    light_up((255, 0, 0))  # Red
    time.sleep(1)
    light_up((0, 255, 0))  # Green
    time.sleep(1)
    light_up((0, 0, 255))  # Blue
    time.sleep(1)
    light_up((255, 255, 255))  # White
    time.sleep(1)
    light_up((0, 0, 0))  # Off
    time.sleep(1)