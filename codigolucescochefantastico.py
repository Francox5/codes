#simulacion -- > https://wokwi.com/projects/391573055586327553
#compilado  -- >  https://github.com/Francox5/codes
from machine import Pin
import time
from utime import sleep
from neopixel import NeoPixel
import _thread

pixel=8

np= NeoPixel(Pin(12), pixel)
rojo=(255,0,0)
degradadorojonaranja=[(255,0,0),(255,32,0),(255,47,0),(255,64,0),(255,72,0),(255,80,0),(255,89,0),(255,96,0)]
degradadonaranja=[(255,96,0),(255,89,0),(255,80,0),(255,72,0),(255,64,0),(255,47,0),(255,32,0),(255,0,0)]
off=(0,0,0)
verde=(85, 166, 48)
amarillo=(255, 255, 63)
degradadoamarillo=[(32,32,255),(64,64,224),(96,96,192),(128,128,160),(160,160,128),(192,192,96),(224,224,64),(255,255,32)]

degradadoverdeazul=[(0,255,32),(0,224,64),(0,192,96),(0,160,128),(0,128,160),(0,96,192),(0,64,224),(0,32,255)]
degradadoazulverde=[(0,32,255),(0,64,224),(0,96,192),(0,128,160),(0,160,128),(0,192,96),(0,224,64),(0,255,32)]
#comentario

def funciona():           
    for i in range(pixel):
        np[i] = degradadorojonaranja[i]
        np.write()
        sleep(0.05)
        np[i] = off
        np.write()
    sleep(1)
    for j in range(pixel - 1, -1, -1):
        np[j]= degradadoamarillo[j]
        np.write()
        sleep(0.05)
        np[j]=off
        np.write()
    sleep(1)
def funcionb():
    for i in range(0 , pixel, 2):
        np[i] = rojo
        np[i+1] = rojo
        np.write()
        sleep(0.09)            
        np[i] = off
        np[i+1] = off
        np.write()    
    for i in range (5, -1 , -2):
        np[i]=rojo
        np[i-1]=rojo
        np.write() 
        sleep(0.09)            
        np[i] = off
        np[i-1] = off
        np.write()    
       
def funcionc():    
    for j in range(4):
        np[j]= amarillo
        np.write()
    sleep(0.1)
    for j in range(4):
        np[j]= off
        np.write()
    sleep(0.1)
    for av in range(2):
        for j in range(4):
            np[j]=verde
            np.write()
        sleep(0.1)
        for j in range(4):
            np[j]= off
            np.write()
        sleep(0.1)
    for j in range(4):
        np[j]= amarillo
        np.write()
    sleep(0.1)
    for j in range(4):
        np[j]= off
        np.write()
    sleep(0.1)

    for j in range(4 , 8):
        np[j]=amarillo
        np.write()
    sleep(0.1)
    for j in range(4 , 8):
        np[j]= off
        np.write()
    sleep(0.1)
    for av in range(2):
        for j in range(4 , 8):
            np[j]=verde
            np.write()
        sleep(0.1)
        for j in range(4 , 8):
            np[j]=off
            np.write()
        sleep(0.1)
    for j in range(4 , 8):
        np[j]=amarillo
        np.write()
    sleep(0.1)
    for j in range(4 ,8):
        np[j]= off
        np.write()
    sleep(0.1)  
def encenderpar():
    for f in range(0 , pixel , 2):
        np[f]=degradadoazulverde[f]
    np.write()
def apagarpar():
    for f in range (0, pixel, 2):
        np[f]=off
    np.write()
def encenderimpar():
    for f in range(1 , pixel, 2):
        np[f]=degradadoazulverde[f]
    np.write()
def apagarimpar():
    for f in range(1,pixel, 2):
        np[f]=off
    np.write()

while True:    
    for n in range(3):
        funciona()

    for m in range(10):
       funcionb()

    for n in range(5):
       funcionc()
       
    
    
   
        

    
      
        
