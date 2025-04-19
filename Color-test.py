from machine import Pin
import time

# Define pins for TCS3200
S2 = Pin(4, Pin.OUT)
S3 = Pin(5, Pin.OUT)
OUT = Pin(3, Pin.IN)

# Calibration values (replace these with your calibrated values)
RED_MIN, RED_MAX = 100, 1200  # Adjust based on your environment
GREEN_MIN, GREEN_MAX = 90, 1100
BLUE_MIN, BLUE_MAX = 80, 1000

# Select color filter
def select_color(color):
    if color == "red":
        S2.off()
        S3.off()
    elif color == "green":
        S2.on()
        S3.on()
    elif color == "blue":
        S2.off()
        S3.on()

# Measure frequency for the selected color
def read_frequency():
    start_time = time.ticks_us()
    pulse_count = 0

    # Count pulses for 100ms
    while time.ticks_diff(time.ticks_us(), start_time) < 100000:
        if OUT.value() == 0:
            while OUT.value() == 0:  # Wait for LOW
                pass
            while OUT.value() == 1:  # Wait for HIGH
                pass
            pulse_count += 1

    return pulse_count

# Normalize raw values to 0–255
def normalize(raw, min_val, max_val):
    if raw < min_val:
        raw = min_val
    if raw > max_val:
        raw = max_val
    return int(((raw - min_val) / (max_val - min_val)) * 255)

# Main function
def main():
    print("Starting color detection...")
    while True:
        try:
            # Measure red light
            select_color("red")
            time.sleep(0.1)
            red_raw = read_frequency()
            red = normalize(red_raw, RED_MIN, RED_MAX)

            # Measure green light
            select_color("green")
            time.sleep(0.1)
            green_raw = read_frequency()
            green = normalize(green_raw, GREEN_MIN, GREEN_MAX)

            # Measure blue light
            select_color("blue")
            time.sleep(0.1)
            blue_raw = read_frequency()
            blue = normalize(blue_raw, BLUE_MIN, BLUE_MAX)

            # Print normalized RGB values
            print(f"Raw -> Red: {red_raw}, Green: {green_raw}, Blue: {blue_raw}")
            print(f"RGB -> Red: {red}, Green: {green}, Blue: {blue}")
            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            break

# Run the program
main()