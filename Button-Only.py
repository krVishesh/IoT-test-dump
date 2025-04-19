from machine import Pin
import time

# Define buttons with internal pull-down resistors
button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)  # Button on GPIO 15
button2 = Pin(21, Pin.IN, Pin.PULL_DOWN)  # Button on GPIO 21
button3 = Pin(22, Pin.IN, Pin.PULL_DOWN)  # Button on GPIO 22
button4 = Pin(19, Pin.IN, Pin.PULL_DOWN)  # Button on GPIO 19

def say_button(num):
    print(f"Button {num} pressed")

while True:
    if button1.value():
        say_button(1)
    if button2.value():
        say_button(2)
    if button3.value():
        say_button(3)
    if button4.value():
        say_button(4)
    
    time.sleep(0.1)  # Add a small delay to avoid spamming
