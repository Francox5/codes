#modulos
from machine import Pin, time_pulse_us
from time import sleep_us, sleep
from neopixel import NeoPixel
from hcsr04 import HCSR04
#crea el objeto neopixel
pixel=8
off=(0,0,0)
np= NeoPixel(Pin(12), pixel)
# Definir los pines del triger y el echo
echo_pin = Pin(26)
trig_pin = Pin(27)
# Crea una instancia del sensor HCSR04
sensor = HCSR04(trigger_pin=trig_pin, echo_pin=echo_pin)
while True:
    # Mide la distancia en centimetros
    distancia = sensor.distance_cm()
    print("Distance: {} cm".format(distancia))            
    #corta espera antes de la siguiente medida
    sleep(0.5)
    #comprueba si hay un objeto a menos de cuatro cm 
    if distancia < 4:
        #cambio de color a rojo para el neopixel
        for i in range(8): 
            np[i]=(255,0,0)
            np.write()
    else:
        #cambio de color a verde 
            for i in range(8):
                np[i]=(0,255,0)
                np.write()



