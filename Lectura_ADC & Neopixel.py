#simulacion --> https://wokwi.com/projects/393487970088615937
#compilado -- > https://github.com/Francox5/codes/
from machine import Pin, ADC    # ADC class is needed to create an ADC object
from time import sleep
import utime
import time
from utime import sleep
from neopixel import NeoPixel 
pixel=8
off=(0,0,0)
np= NeoPixel(Pin(12), pixel)
# creating an ADC object, specifying GPIO Pin 28 as the INPUT pin
adc = ADC(Pin(26))
# Note: GPIO Pins capable of ADC are GPIO Pin 26-28 only

# continuously read data from the potentiometer and display the values to the console
while True:
    # reading analog values from the potentiometer
    conversion = adc.read_u16()
    print(f"Analog value: {conversion}")

    # converting analog values to voltage
    voltage = conversion * (3.3 / 65535)
    print(f"Voltage: {voltage}")

    print("==========")
    
    if conversion > 7500:
        np[0]=(255, 32 ,0)
        np.write()
        for i in range(1, 8):
            np[i]=off
            np.write()
    if conversion > 15000:
        np[1]=(224, 64 ,0)
        np.write()
        for i in range(2, 8):
            np[i]=off
            np.write()
    if conversion > 22500:
        np[2]=(192, 96 ,0)
        np.write()
        for i in range(3, 8):
            np[i]=off
            np.write()
    if conversion > 30000:
        np[3]=(160, 128 ,0)
        np.write()
        for i in range(4, 8):
            np[i]=off
            np.write()
    if conversion > 37500:
        np[4]=(128, 160 ,0)
        np.write()
        for i in range(5, 8):
            np[i]=off
            np.write()
    if conversion > 45000:
        np[5]=(96, 192 ,0)
        np.write()
        for i in range(6, 8):
            np[i]=off
            np.write()
    if conversion > 52500:
        np[6]=(64, 224 ,0)      
        np.write()
        for i in range(7, 8):
            np[i]=off
            np.write()
    if conversion > 60000:
        np[7]=(32, 255 ,0)
        np.write()
    if conversion < 7500:
        for i in range(8):
            np[i]=(0,0,0)
            np.write()
    
