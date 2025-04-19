import network
import time
from secrets import WIFI_SSID, WIFI_PASSWORD

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

connect_wifi()