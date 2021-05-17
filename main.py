from config import utelegram_config
from config import wifi_config
from boot import do_connect

import utelegram
import network
import utime

from machine import Pin
from blink import blink

pir = Pin(4, Pin.IN)

def handle_motion(pin):
  print('Motion!')
  blink()
  bot.send(<bot_chat_id>, 'Motion! ')


sta_if = network.WLAN(network.STA_IF)

def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())
    print(message)

def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'pong')
    
def do_main():
  if sta_if.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/ping', reply_ping)
    bot.set_default_handler(get_message)
    pir.irq(trigger=Pin.IRQ_RISING, handler=handle_motion)
    print('BOT LISTENING')
    bot.listen()
    
  else:
    print('NOT CONNECTED - trying to connect again')
    do_connect()
    do_main()    

do_main()



