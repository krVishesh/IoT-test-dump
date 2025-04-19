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
    bits=32,  # Supports 24-bit playback
    format=I2S.MONO,
    rate=8000,
    ibuf=2048
)

# Function to Write 24-bit WAV Header
def write_wav_header(file, sample_rate, num_channels, bit_depth):
    file.write(b'RIFF')  
    file.write(struct.pack('<I', 36))  # Placeholder for file size
    file.write(b'WAVEfmt ')  
    file.write(struct.pack('<IHHIIHH', 16, 1, num_channels, sample_rate, sample_rate * num_channels * 3, num_channels * 3, bit_depth))
    file.write(b'data')  
    file.write(struct.pack('<I', 0))  # Placeholder for data size

# Start Recording
print("Press and hold button to record")
wait_for_button()
print("Recording...")

samples = bytearray(2048)

with open("test_24bit.wav", "wb") as file:
    write_wav_header(file, 8000, 1, 24)  # Write WAV header

    while record_pin.value(0) == 1:
        read_bytes = audio_in.readinto(samples)
        I2S.shift(buf=samples, bits=32, shift=3)  # Amplify by 8×
        converted_samples = bytearray()

        for i in range(0, read_bytes, 4):  # Convert 32-bit to 24-bit
            sample_32 = struct.unpack_from("<i", samples, i)[0]
            sample_24 = sample_32 >> 8  # Keep upper 24 bits
            converted_samples.extend(struct.pack("<i", sample_24)[:3])  # Store only 3 bytes

        file.write(converted_samples)

print("Finished Recording")

# Playback Recorded Audio
print("Press the button to playback")
wait_for_button()
print("Playing back...")

with open("test_24bit.wav", "rb") as file:
    file.seek(44)  # Skip WAV header
    samples_read = file.readinto(samples)
    
    while samples_read > 0:
        converted_samples = bytearray()
        
        for i in range(0, samples_read, 3):  # Read packed 24-bit PCM
            if i + 2 < samples_read:
                # Read 24-bit sample (big-endian order)
                sample_24 = samples[i] | (samples[i+1] << 8) | (samples[i+2] << 16)

                # Convert to 32-bit left-aligned PCM
                sample_32 = sample_24 << 8  # Shift left to align with 32-bit frame
                
                # Store as signed 32-bit PCM
                converted_samples.extend(struct.pack("<i", sample_32))

        audio_out.write(converted_samples)  # Send correctly aligned data to DAC
        samples_read = file.readinto(samples)

#     while samples_read > 0:
#         audio_out.write(samples[:samples_read])  # Send to DAC
#         samples_read = file.readinto(samples)

print("Finished Playback")
