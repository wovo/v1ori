import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def blink( pin, delay = 0.5 ):
   GPIO.setup( pin, GPIO.OUT )
   while True:
      GPIO.output( pin, GPIO.HIGH )
      time.sleep( delay )
      GPIO.output( pin, GPIO.LOW )
      time.sleep( delay )

print( "blink demo - function" )

blink( 18, 0.2 )
