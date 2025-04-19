from machine import ADC, Pin
import time

adc = ADC(Pin(1))  
adc.atten(ADC.ATTN_11DB)  

while True:
    raw_value = adc.read()  
    print(f"🔥 Flame Intensity: {raw_value}")

    if raw_value < 1500:  
        print("🔥 Fire Detected!")

    time.sleep(1)
