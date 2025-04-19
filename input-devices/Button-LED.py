from machine import Pin
import time

# Define LED and Button pins
led = Pin(13, Pin.OUT)  # LED on GPIO 12
button = Pin(10, Pin.IN)  # Button on GPIO 11 with internal pull-up

def blink_led(num):
    for i in range(num):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

while True:
    if button.value() == 1:  # Button pressed (active-low)
        blink_led(2)  # Blink LED twice when button is pressed
    else:
        led.off()  # Ensure LED stays off when not pressing
    time.sleep(0.05)  # Small debounce delay
