#Example usage for ESP32
from machine import Pin, ADC
from time import sleep

# analog inputs for X and Y
analogPinX = ADC(Pin(3)) # 0R, 3L
analogPinY = ADC(Pin(2)) # 1R, 2L

#switching the analog input to 12Bit (0...4095)
analogPinX.atten(ADC.ATTN_11DB)
analogPinY.atten(ADC.ATTN_11DB)

# digital input on pin 14
sw = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor 5 (right), 4 (left)

while True:
  analogValX = analogPinX.read()
  analogValY = analogPinY.read()
  switch = sw.value()

  print("x:%s   y:%s   sw:%s" % (analogValX, analogValY, switch))
 
  sleep(0.1)