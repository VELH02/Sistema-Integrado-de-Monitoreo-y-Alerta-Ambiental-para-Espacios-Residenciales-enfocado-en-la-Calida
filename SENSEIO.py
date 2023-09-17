#Escrito por Victor Lau 07/08/2019
#importando librerias

from Adafruit_IO import *
from sense_hat import SenseHat
import time
from gpiozero import CPUTemperature
#conectandose a Adafruit IO
aio = Client("VELH","03dd04e47a874cb4a4c327ed6e56fac8")
while 1>0:
    #recolectando datos de las variables 
    sense = SenseHat()
    sense.clear()
    t = sense.get_temperature()
    cpu = CPUTemperature()
    cput = cpu.temperature
    p = sense.get_pressure()
    h = sense.get_humidity()
    tr = cput-(cput-t/1.5)
    #enviando datos de las variales(sensores)
    aio.send("temperatura", tr)
    aio.send("presion", p)
    aio.send("humedad", h)
    print("sending...")
    time.sleep(60)
    

