import network
import espnow
import json

# Initialize ESP-NOW
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
esp = espnow.ESPNow()
esp.active(True)

print("Waiting for data...")

while True:
    peer_mac, msg = esp.recv()
    if msg:  # Check if a valid message is received
        try:
            data_str = msg.decode()
            data = eval(data_str)  # Convert string to dictionary (use `json.loads` in safe cases)

            # Extract device info
            device_id = data.get("Device", -1)  # Get the active device
            print(f"Received for Device {device_id+1}: {data}")

        except Exception as e:
            print("Error decoding:", e)
