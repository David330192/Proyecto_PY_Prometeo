from machine import Pin
import utime

#interuptor = Pin(4,Pin.IN,Pin.PULL_UP)
ledR = Pin(5,Pin.OUT)
ledV = Pin(18,Pin.OUT)
ledA = Pin(21,Pin.OUT)

#Funcion para asigar los colores del RGB 
def Colores(a,b,c):
    ledR(a)
    ledV(b)
    ledA(c)

#Valida que accion a ingresado el usuario 0 = huella no registrada, 1 huella registrada
valor = int(input("Ingrese la huella: "))
if valor == 0:
    Colores(0,1,0); print("No esta autorizado, sonar la alarma");utime.sleep(2) #Color Rojo
    Colores(0,0,0); print("Led Apagado");utime.sleep(2) #Apaga el led
if valor == 1:
    Colores(1,1,0); print("Autorizado ");utime.sleep(2) #Color verde
    Colores(0,1,1); print("Enciende la motocileta ");utime.sleep(2) #Color Magenta
    Colores(0,0,0); print("Led Apagado");utime.sleep(2) #Apaga el led

    
        
        
    




