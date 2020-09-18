import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, delay1, delay2 ):
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( delay1 )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( delay2 )

def morse( pin, delay, text ):
   GPIO.setup( 18, GPIO.OUT )
   for c in text:
      if c == " ":
         pulse( pin, 0, 3 * delay )         
      elif c == ".":
         pulse( pin, delay, delay )         
      elif c == "-":
         pulse( pin, 3 * delay, delay )         
      elif c == "-":
         print( "non-morse character '%s'" % c )    


print( "blink demo - morse" )

morse( 18, 0.2, ".--. -.-- - .... --- -." )
