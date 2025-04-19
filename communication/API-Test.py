from machine import Pin, SDCard
import network
import time
import urequests
import binascii
import json
import os
from secrets import WIFI_SSID, WIFI_PASSWORD, API_KEY

global transcript

# Setup record button
record_pin = Pin(10, Pin.IN)

def wait_for_button():
    while record_pin.value() == 0:
        time.sleep_ms(100)
    time.sleep_ms(100)
    
def encode_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            encoded_audio = binascii.b2a_base64(f.read()).decode("utf-8").replace("\n", "")
        return encoded_audio
    except Exception as e:
        print("❌ Error Encoding File:", e)
        return None

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)  # Set ESP32 as a station (client)
    wlan.active(True)  # Activate Wi-Fi

    if not wlan.isconnected():
        print(f"🔌 Connecting to {WIFI_SSID}...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        # Wait for connection
        for _ in range(10):
            if wlan.isconnected():
                print("✅ Connected! IP Address:", wlan.ifconfig()[0])
                return True
            time.sleep(1)
            
    if wlan.isconnected():
        print("✅ Connected! IP Address:", wlan.ifconfig()[0])
        return True

    print("❌ Wi-Fi Connection Failed!")
    return False

def send_to_gemini():
    if not transcript:
        print("⚠️ No transcription to send to Gemini.")
        return None
    else:
        print(f"Transcript = {transcript}")
        
    print("🚀 Sending to Gemini AI...")
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    content = transcript + ", Answer in a Single line"
    data = json.dumps({
        "contents": [{"parts": [{"text": content}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 20
        }
    })

    try:
        response = urequests.post(url, data=data, headers=headers)
        result = response.json()
        response.close()

        if "candidates" in result:
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
            print("🤖 Gemini AI Response:", answer)
            return answer
        else:
            print("❌ No response from Gemini:", result)
            return None
    except Exception as e:
        print("❌ Gemini API Request Failed:", e)
        return None

connect_wifi()

print("Press Button")
wait_for_button()

# SD Card Pins
clk = Pin(2)
mosi = Pin(8)
miso = Pin(9)
cs = Pin(7)

# Initialize SD Card
try:
    sd = SDCard(slot=2, sck=clk, mosi=mosi, miso=miso, cs=cs)
    os.mount(sd, "/sd")
    print("✅ SD Card Mounted Successfully!")
except Exception as e:
    print("❌ SD Card Error:", e)
    sd = None

# List all files on SD Card
if sd:
    print("\n📂 Files on SD Card:")
    try:
        for file_name in os.listdir("/sd"):
            print(f" - {file_name}")
    except Exception as e:
        print("❌ Error Listing Files:", e)

print("Press Button")
wait_for_button()

if sd:
    if connect_wifi():
        AUDIO_FILE = "/sd/recorded_audio.wav"

        # Encode the audio file
        audio_base64 = encode_audio(AUDIO_FILE)
        if not audio_base64:
            print("❌ Failed to encode audio.")
        else:
            print("✅ Audio Encoded Successfully.")

        # Google STT API Endpoint
        url = f"https://speech.googleapis.com/v1/speech:recognize?key={API_KEY}"

        # Request Payload
        headers = {"Content-Type": "application/json"}
        data = json.dumps({
            "config": {
                "encoding": "LINEAR16",
                "sampleRateHertz": 8000,
                "languageCode": "en-IN"
            },
            "audio": {
                "content": audio_base64
            }
        })

        # Send POST Request
        try:
            response = urequests.post(url, data=data, headers=headers)
            result = response.json()
            response.close()
            
            # Extract and print the transcript
            if "results" in result:
                transcript = result["results"][0]["alternatives"][0]["transcript"]
                print("📝 Transcription:", transcript)
            else:
                print("❌ No transcription found:", result)
        except Exception as e:
            print("❌ API Request Failed:", e)
    else:
        print("⚠️ Cannot send request: No internet")

print("Press Button")
wait_for_button()

if sd:
    if connect_wifi():
        gemini_response = send_to_gemini()
        print("✅ Final Response:", gemini_response)

# Unmount SD Card
if sd:
    os.umount("/sd")
    print("✅ SD Card Unmounted Successfully!")