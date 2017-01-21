from gpiozero import LED
from time import sleep
led = LED(21)
tr  = 1

while (tr == 1):
    sleep(0.5)
    led.on()
    sleep(0.5)
    led.off()
   
