import machine
import neopixel
import time

NUM_LEDS = 16  # Number of LEDs in the strip
PIN = 1       # GPIO pin connected to the WS2812 data line (change as needed)

np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

def clear():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def color_wipe(color, delay=50):
    for i in range(NUM_LEDS):
        np[i] = color
        np.write()
        time.sleep_ms(delay)

def rainbow_cycle(delay=10):
    for j in range(256):
        for i in range(NUM_LEDS):
            np[i] = wheel((i * 256 // NUM_LEDS + j) & 255)
        np.write()
        time.sleep_ms(delay)

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

while True:
    color_wipe((255, 0, 0), 50)  # Red
    color_wipe((0, 255, 0), 50)  # Green
    color_wipe((0, 0, 255), 50)  # Blue
    rainbow_cycle(10)
    color_wipe((255, 255, 255), 0)  # White
    time.sleep(3)
