from machine import I2S, Pin
import time
import struct

# Setup record button
record_pin = Pin(10, Pin.IN)

def wait_for_button():
    while record_pin.value() == 0:
        time.sleep_ms(100)
    time.sleep_ms(100)

# I2S Pins for INMP441 Mic
mic_sck_pin = Pin(1)  # BCLK
mic_ws_pin = Pin(4)   # LRCLK
mic_sd_pin = Pin(3)   # DOUT

# I2S Pins for MAX98357A Speaker
spk_bck_pin = Pin(1)  # BCLK
spk_ws_pin = Pin(5)   # LRCLK
spk_sdout_pin = Pin(6) # DIN

# Setup I2S for Microphone (INMP441)
audio_in = I2S(
    0,
    sck=mic_sck_pin,
    ws=mic_ws_pin,
    sd=mic_sd_pin,
    mode=I2S.RX,
    bits=32,  # INMP441 provides 32-bit PCM
    format=I2S.MONO,
    rate=8000,
    ibuf=2048
)

# Setup I2S for Speaker (MAX98357A)
audio_out = I2S(
    1,
    sck=spk_bck_pin,
    ws=spk_ws_pin,
    sd=spk_sdout_pin,
    mode=I2S.TX,
    bits=32,  # Supports 16-bit playback (left-aligned inside 32-bit frame)
    format=I2S.MONO,
    rate=8000,
    ibuf=2048
)

# Function to Write Proper WAV Header (LINEAR16)
def write_wav_header(file, sample_rate, num_channels, bit_depth, data_size):
    file.write(b'RIFF')
    file.write(struct.pack('<I', 36 + data_size))  # Correct file size
    file.write(b'WAVEfmt ')
    file.write(struct.pack('<IHHIIHH', 16, 1, num_channels, sample_rate, sample_rate * num_channels * 2, num_channels * 2, bit_depth))
    file.write(b'data')
    file.write(struct.pack('<I', data_size))  # Correct data size

# Start Recording
print("Press and hold button to record")
wait_for_button()
print("Recording...")

samples = bytearray(2048)
converted_samples = bytearray()

while record_pin.value() == 1:
    read_bytes = audio_in.readinto(samples)

    # Amplify sound safely
    I2S.shift(buf=samples, bits=32, shift=3)  # Amplify by 8×

    for i in range(0, read_bytes, 4):  # Convert 32-bit to 16-bit
        sample_32 = struct.unpack_from("<i", samples, i)[0]
        sample_16 = struct.pack("<h", sample_32 >> 16)  # Convert to signed 16-bit PCM
        converted_samples.extend(sample_16)

print("Finished Recording")

# Write to WAV file
with open("test_16bit.wav", "wb") as file:
    write_wav_header(file, 8000, 1, 16, len(converted_samples))  # Correct header
    file.write(converted_samples)

print("Saved as 16-bit PCM WAV")

# Playback Recorded Audio
print("Press the button to playback")
wait_for_button()
print("Playing back...")

samples_read = 0
while samples_read < len(converted_samples):
    playback_samples = bytearray()
    
    for i in range(samples_read, min(samples_read + 2048, len(converted_samples)), 2):
        # Read 16-bit PCM sample
        sample_16 = struct.unpack_from("<h", converted_samples, i)[0]
        
        # Convert to 32-bit left-aligned for MAX98357A
        sample_32 = sample_16 << 16
        playback_samples.extend(struct.pack("<i", sample_32))

    audio_out.write(playback_samples)
    samples_read += 2048

print("Finished Playback")
