from machine import Pin, PWM
from time import sleep

# Define motor control pins for Motor A
motor_A_IN1 = PWM(Pin(2), freq=1000)
motor_A_IN2 = PWM(Pin(3), freq=1000)

# Define motor control pins for Motor B (optional)
motor_B_IN3 = PWM(Pin(7), freq=1000)
motor_B_IN4 = PWM(Pin(8), freq=1000)

def motor_A_forward(speed=512):
    motor_A_IN1.duty_u16(speed)  # Set speed (0-65535)
    motor_A_IN2.duty_u16(0)      # Stop IN2

def motor_A_backward(speed=512):
    motor_A_IN1.duty_u16(0)      # Stop IN1
    motor_A_IN2.duty_u16(speed)  # Set speed

def motor_A_stop():
    motor_A_IN1.duty_u16(0)
    motor_A_IN2.duty_u16(0)

# Motor B functions (if second motor is used)
def motor_B_forward(speed=512):
    motor_B_IN3.duty_u16(speed)
    motor_B_IN4.duty_u16(0)

def motor_B_backward(speed=512):
    motor_B_IN3.duty_u16(0)
    motor_B_IN4.duty_u16(speed)

def motor_B_stop():
    motor_B_IN3.duty_u16(0)
    motor_B_IN4.duty_u16(0)

# Testing the motors
while True:
    print("Motor A Forward")
    motor_A_forward(15000)
    sleep(2)
    
    print("Motor A Stop")
    motor_A_stop()
    sleep(3)

    print("Motor A Backward")
    motor_A_backward(15000)
    sleep(2)

    print("Motor A Stop")
    motor_A_stop()
    sleep(3)
