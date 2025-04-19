from machine import Pin
import time

user_led = 21
LED_PIN = Pin(user_led, Pin.OUT)

def blink():
    LED_PIN.off()
    time.sleep(0.5)
    LED_PIN.on()
    time.sleep(0.5)


blink()
blink()