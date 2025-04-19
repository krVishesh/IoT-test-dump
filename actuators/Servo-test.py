from machine import Pin, PWM
from time import sleep

# Define the PWM pin and frequency
servo = PWM(Pin(26), freq=50)

def set_angle(angle):
    """Convert angle (0-180) to duty cycle and apply it smoothly."""
    min_duty, max_duty = 20, 120  # Adjust if needed
    duty = int((angle / 180) * (max_duty - min_duty) + min_duty)
    servo.duty(duty)

def smooth_move(start, end, step=1, delay=0.02):
    """Gradually move the servo between two angles."""
    step = step if start < end else -step
    for angle in range(start, end + step, step):
        set_angle(angle)
        sleep(delay)

while True:
    smooth_move(0, 180, step=1, delay=0.02)  # Move smoothly from 0° to 180°
    sleep(1)
    smooth_move(180, 0, step=1, delay=0.02)  # Move smoothly back
    sleep(3)
