from machine import Pin, SPI
from mfrc522 import MFRC522
import time

# Initialize SPI and RFID module
spi = SPI(2, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
rfid = MFRC522(spi, cs=Pin(5, Pin.OUT))

print("Scan an RFID tag...")

while True:
    (status, tag_type) = rfid.request(rfid.REQIDL)

    if status == rfid.OK:
        (status, uid) = rfid.anticoll()
        if status == rfid.OK and isinstance(uid, list):
            tag_uid = ":".join(f"{i:02X}" for i in uid)
            print("RFID Tag Detected! UID:", tag_uid)
            time.sleep(1)  # Avoid duplicate reads
