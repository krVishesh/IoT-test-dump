from machine import Pin, I2C
import bluetooth
from ble_hid import BLEMouse
import time

# Setup AS5600 Magnetic Encoder
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
addr = 0x36  # AS5600 I2C address

def read_angle():
    raw = i2c.readfrom_mem(addr, 0x0E, 2)  # Read 2 bytes from register 0x0E
    angle = (raw[0] << 8 | raw[1]) & 0x0FFF  # Extract 12-bit angle
    return angle

# Initialize BLE Mouse
ble = bluetooth.BLE()
mouse = BLEMouse(ble)

last_angle = read_angle()

while True:
    if mouse.is_connected():
        angle = read_angle()
        delta = angle - last_angle

        # Handle rollover
        if delta > 2048:
            delta -= 4096
        if delta < -2048:
            delta += 4096

        scroll = delta // 100  # Adjust sensitivity

        if scroll != 0:
            mouse.move(0, 0, scroll)  # Move only the scroll wheel

        last_angle = angle
        time.sleep(0.05)  # Adjust for responsiveness
