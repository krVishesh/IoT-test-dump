from machine import I2S, Pin
import math
import struct
import time

# Set up I2S for speaker output
spk_bck_pin = Pin(1)
spk_ws_pin = Pin(5)
spk_sdout_pin = Pin(6)

audio_out = I2S(
    0,
    sck=spk_bck_pin,
    ws=spk_ws_pin,
    sd=spk_sdout_pin,
    mode=I2S.TX,
    bits=32,
    format=I2S.MONO,
    rate=8000,
    ibuf=2048
)

# Constants for sine wave generation
sample_rate = 8000  # Hz
frequency = 440  # Hz (A4 tone)
duration = 2  # seconds

# Generate and play a sine wave
print("Playing test tone at 440 Hz (A4)")

num_samples = sample_rate * duration

buffer = bytearray()
for i in range(num_samples):
    sample_value = int(32767 * math.sin(2 * math.pi * frequency * i / sample_rate))
    buffer.extend(struct.pack("<i", sample_value << 16))  # Align to 32-bit format

audio_out.write(buffer)  # Send the entire buffer at once
    
print("Finished test tone")
