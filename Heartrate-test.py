from machine import SoftI2C, Pin
from utime import sleep, ticks_ms
from max30102.circular_buffer import CircularBuffer
from max30102 import MAX30102

# Initialize I2C
sda = Pin(14)  # Change to your board's SDA pin
scl = Pin(15)  # Change to your board's SCL pin
i2c = SoftI2C(sda=sda, scl=scl)

# Initialize MAX30102 sensor
sensor = MAX30102(i2c)
sensor.setup_sensor()

print("MAX30102 initialized. Reading heart rate data...")

# Heart rate calculation variables
ir_values = []
time_stamps = []
peak_threshold = 5000  # Adjust based on sensor data
min_peak_interval = 300  # Minimum time (ms) between peaks to avoid false readings

def calculate_heart_rate():
    if len(time_stamps) < 2:
        return None  # Not enough data
    
    intervals = [time_stamps[i + 1] - time_stamps[i] for i in range(len(time_stamps) - 1)]
    avg_interval = sum(intervals) / len(intervals)
    bpm = 60000 / avg_interval  # Convert ms to BPM
    return int(bpm)

try:
    last_peak_time = 0
    while True:
        ir_value = sensor.get_ir()
        red_value = sensor.get_red()
#         print(f"❤️ IR: {ir_value}, 🔴 Red: {red_value}")
        
        current_time = ticks_ms()
        
        # Peak detection logic with threshold and time interval
        if (
            len(ir_values) > 2 and
            ir_values[-2] < ir_values[-1] > ir_value and  # Detect peak
            ir_values[-1] > peak_threshold and  # Ensure it's a valid peak
            (current_time - last_peak_time) > min_peak_interval  # Prevent double counting
        ):
            time_stamps.append(current_time)
            last_peak_time = current_time
            if len(time_stamps) > 10:
                time_stamps.pop(0)  # Keep last 10 peaks
            
            bpm = calculate_heart_rate()
            if bpm and 40 < bpm < 180:  # Filter out unrealistic values
                print(f"💓 Heart Rate: {bpm} BPM")
        
        ir_values.append(ir_value)
        if len(ir_values) > 10:
            ir_values.pop(0)  # Keep last 10 readings
        
        sleep(0.1)
except KeyboardInterrupt:
    print("Stopping sensor readings.")
