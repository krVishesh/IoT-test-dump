from machine import Pin, PWM
import time

# Define motor control pins
IN1 = PWM(Pin(32))  # Connect to DRV8833 IN1
IN2 = PWM(Pin(33))  # Connect to DRV8833 IN2

# Set PWM frequency
IN1.freq(1000)
IN2.freq(1000)

def motor_forward(speed=512):
    """Run motor forward at given speed (0-1023)"""
    IN1.duty(speed)
    IN2.duty(0)

def motor_backward(speed=512):
    """Run motor backward at given speed"""
    IN1.duty(0)
    IN2.duty(speed)

def motor_stop():
    """Stop motor"""
    IN1.duty(0)
    IN2.duty(0)

# Test sequence
while True:
    print("Motor Forward")
    motor_forward(600)
    time.sleep(2)
    
    print("Motor Stop")
    motor_stop()
    time.sleep(2)

    print("Motor Backward")
    motor_backward(600)
    time.sleep(2)

    print("Motor Stop")
    motor_stop()
    time.sleep(2)
