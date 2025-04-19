from machine import Pin, PWM
import time

# Initialize PWM on pin 3 with a frequency of 10 kHz
motor = PWM(Pin(6), freq=18000, duty_u16=0)  

def set_speed(speed):
    """Set motor speed from 0 to 100% (0 to 65535 duty cycle)."""
    duty = int((speed / 100) * 65535)  # Convert percentage to 16-bit value
    motor.duty_u16(duty)

try:
    while True:
        for speed in range(0, 101, 10):  # Increase speed from 0% to 100%
            set_speed(speed)
            print(f"Speed: {speed}%")
            time.sleep(1)
        
        for speed in range(100, -1, -10):  # Decrease speed from 100% to 0%
            set_speed(speed)
            print(f"Speed: {speed}%")
            time.sleep(1)

except KeyboardInterrupt:
    motor.duty_u16(0)  # Turn off the motor
    print("Motor stopped")
