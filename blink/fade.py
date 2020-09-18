import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, duration, intensity ):
   print( duration, intensity )
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( duration * intensity )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( duration - ( duration * intensity ) )

def fade( pin, delay ):
   GPIO.setup( pin, GPIO.OUT )
   while True:
      steps = 1000
      for i in range( 0, steps ):
         pulse( pin, delay / steps, i / ( 1.0 * steps ) )
      for i in range( 0, steps ):
         pulse( pin, delay / steps, ( steps - i ) / ( 1.0 * steps ) )

print( "demo - fade" )

fade( 18, 2.0 )
