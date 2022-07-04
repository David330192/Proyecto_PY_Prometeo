from machine import Pin
import bluetooth
from BLE import BLEUART

bombillo= Pin(15, Pin.OUT)

name= "ESPJesus" 

ble = bluetooth.BLE()
uart = BLEUART(ble, name)


def on_rx():
    
    rx_recibe = uart.read().decode().strip()
    uart.write("EspJesus dice: " + str(rx_recibe) + "\n")
    
    if rx_recibe == "on":
        bombillo.value(1)
        print("encendiendo bombillo")
        uart.write("EspJesus dice: " + "encendiendo" + "\n")
        
    if rx_recibe == "off":
        bombillo.value(0)
        print("apagando bombillo")
        uart.write("EspJesus dice: " + "apagando" + "\n")
    
    
uart.irq(handler = on_rx)