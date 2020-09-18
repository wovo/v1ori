import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )

def pulse( pin, delay1, delay2 ):
   GPIO.output( pin, GPIO.HIGH )
   time.sleep( delay1 )
   GPIO.output( pin, GPIO.LOW )
   time.sleep( delay2 )

def morse_codes( pin, delay, text ):
   GPIO.setup( 18, GPIO.OUT )
   for c in text:
      if c == " ":
         pulse( pin, 0, 3 * delay )         
      elif c == ".":
         pulse( pin, delay, delay )         
      elif c == "-":
         pulse( pin, 3 * delay, delay )         
      elif c == "x":
         pulse( pin, 7 * delay, delay )         
      elif c == "-":
         print( "non-morse character '%s'" % c )  

morse_table = {
   "a" : ".-",
   "b" : "-...",
   "c" : "-.-.",
   "d" : "-..",
   "e" : ".",
   "f" : "..-.",
   "g" : "--.",
   "h" : "....",
   "i" : "..",
   "j" : ".---",
   "k" : "-.-",
   "l" : ".-..",
   "m" : "--",
   "n" : "-.",
   "o" : "----",
   "p" : ".---.",
   "q" : "--.-",
   "r" : ".-.",
   "s" : "....",
   "t" : "-",
   "u" : "..-",
   "v" : "...-",
   "w" : ".--",
   "x" : "-..-",
   "y" : "-.--",
   "z" : "--..",
   " " : "x",
}

def morse_text( pin, delay, text ):
   s = ""
   for c in text:
      c = c.lower()
      if c in morse_table:
         s += morse_table[ c ] + " "
   morse_codes( pin, delay, s )        


print( "blink demo - morse text" )

morse_text( 18, 0.2, "Hello world" )
