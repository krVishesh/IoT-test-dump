import os
from machine import Pin, SDCard

#Define Pins
clk = Pin(2)
mosi = Pin(8)
miso = Pin(9)
cs = Pin(7)
# Reassign SD_MMC pins (ESP32-S3 supports this feature)
sd = SDCard(slot=2, sck=clk, mosi=mosi, miso=miso, cs=cs)

try:
    os.mount(sd, "/sd")
    print("✅ SD Card Mounted Successfully!")
    print("PASS")

    # Get SD card details
    stat = os.statvfs("/sd")
    total_space = stat[0] * stat[2]  # Block size * total blocks
    free_space = stat[0] * stat[3]   # Block size * free blocks

    print(f"💾 Total Space: {total_space / (1024 * 1024):.2f} MB")
    print(f"📂 Free Space: {free_space / (1024 * 1024):.2f} MB")

    # List files on SD card
    print("\n📄 Files on SD card:")
    for file in os.listdir("/sd"):
        print(" -", file)
    
    # Unmount the SD card
    os.umount("/sd")
    print("✅ SD Card Unmounted Successfully!")

except Exception as e:
    print("❌ SD Card Error:", e)
