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
      pulse( pin, 0.2, 0.2 )
      pulse( pin, 0.2, 0.2 )
      pulse( pin, 0.5, 1.0 )

print( "blink demo - ssl" )

blink( 18, 0.2 )
