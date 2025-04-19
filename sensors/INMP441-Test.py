from machine import I2S
from machine import Pin
import time

record_pin = Pin(10, Pin.IN)

def wait_for_button():
    while record_pin.value() == 0:
        time.sleep_ms(100)
    time.sleep_ms(100)

mic_sck_pin = Pin(1)
mic_ws_pin = Pin(4)
mic_sd_pin = Pin(3)

audio_in = I2S(
    0,
    sck=mic_sck_pin,
    ws=mic_ws_pin,
    sd=mic_sd_pin,
    mode=I2S.RX,
    bits=32,
    format=I2S.MONO,
    rate=16000,
    ibuf=100000
)

spk_bck_pin = Pin(1)
spk_ws_pin = Pin(5)
spk_sdout_pin = Pin(6)

audio_out = I2S(
    1,
    sck=spk_bck_pin,
    ws=spk_ws_pin,
    sd=spk_sdout_pin,
    mode=I2S.TX,
    bits=32,
    format=I2S.MONO,
    rate=16000,
    ibuf=100000
)

print("Press and hold button to record")

wait_for_button()

print("Recording")

samples = bytearray(8192)

with open("test.raw", "wb") as file:
    while record_pin.value() == 1:
        read_bytes = audio_in.readinto(samples)
        # amplify the signal to make it more audible
        I2S.shift(buf=samples, bits=32, shift=4)
        file.write(samples[:read_bytes])

print("Finished Recording")

print("Processing data")

print("Press the button to playback")

wait_for_button()

with open("test.raw", "rb") as file:
    samples_read = file.readinto(samples)
    while samples_read > 0:
        audio_out.write(samples[:samples_read])
        samples_read = file.readinto(samples)

print("Finished playback")