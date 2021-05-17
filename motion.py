#used for testing if PIR-sensor works 
from machine import Pin
from blink import blink

pir = Pin(4, Pin.IN)

def handle_motion(pin):
  print('Motion!')
  blink()

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_motion)

