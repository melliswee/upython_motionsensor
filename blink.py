import time
from machine import Pin
led=Pin(2,Pin.OUT)

def blink():
    led.value(1)
    time.sleep(1)
    led.value(0)

