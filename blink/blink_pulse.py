import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, delay1, delay2 ):
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( delay1 )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( delay2 )

def blink( pin, delay = 0.5 ):
   GPIO.setup( pin, GPIO.OUT )
   while True:
      pulse( pin, delay, delay )

print( "blink demo - pulse" )

blink( 18, 0.2 )
