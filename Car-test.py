from machine import Pin, PWM
import time

# Define motor pins for first DRV8833
drv1_in1 = PWM(Pin(10))
drv1_in2 = PWM(Pin(11))
drv1_in3 = PWM(Pin(12))
drv1_in4 = PWM(Pin(13))

# Define motor pins for second DRV8833
drv2_in1 = PWM(Pin(2))
drv2_in2 = PWM(Pin(3))
drv2_in3 = PWM(Pin(5))
drv2_in4 = PWM(Pin(6))

# Set PWM frequency
drv1_in1.freq(1000)
drv1_in2.freq(1000)
drv1_in3.freq(1000)
drv1_in4.freq(1000)
drv2_in1.freq(1000)
drv2_in2.freq(1000)
drv2_in3.freq(1000)
drv2_in4.freq(1000)

def motor_control(in1, in2, speed):
    if speed > 0:
        in1.duty_u16(abs(speed))
        in2.duty_u16(0)
    elif speed < 0:
        in1.duty_u16(0)
        in2.duty_u16(abs(speed))
    else:
        in1.duty_u16(0)
        in2.duty_u16(0)

while True:
    # Forward
    motor_control(drv1_in1, drv1_in2, 10000)
    motor_control(drv1_in3, drv1_in4, 10000)
    motor_control(drv2_in1, drv2_in2, 10000)
    motor_control(drv2_in3, drv2_in4, 10000)
    time.sleep(2)
    
    # Stop
    motor_control(drv1_in1, drv1_in2, 0)
    motor_control(drv1_in3, drv1_in4, 0)
    motor_control(drv2_in1, drv2_in2, 0)
    motor_control(drv2_in3, drv2_in4, 0)
    time.sleep(1)
    
    # Reverse
    motor_control(drv1_in1, drv1_in2, -10000)
    motor_control(drv1_in3, drv1_in4, -10000)
    motor_control(drv2_in1, drv2_in2, -10000)
    motor_control(drv2_in3, drv2_in4, -10000)
    time.sleep(2)
    
    # Stop
    motor_control(drv1_in1, drv1_in2, 0)
    motor_control(drv1_in3, drv1_in4, 0)
    motor_control(drv2_in1, drv2_in2, 0)
    motor_control(drv2_in3, drv2_in4, 0)
    time.sleep(1)
