from machine import Pin, PWM
import time

motor_pwm = PWM(Pin(6), freq=20000, duty_u16=0)  # 20kHz PWM

def set_speed(speed):
    duty = int((speed / 100) * 65535)
    motor_pwm.duty_u16(duty)

try:
    set_speed(100)  # Start with full speed to test
    time.sleep(2)   # Give the motor time to start
    set_speed(50)   # Reduce speed to 50%
    time.sleep(2)
    set_speed(0)    # Stop motor
    print("Test complete.")

except KeyboardInterrupt:
    set_speed(0)
    print("Motor stopped")
