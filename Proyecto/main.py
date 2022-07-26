from sensores import SensoresP #Modulo sensores del proyecto Prometeo
from as608 import As608 #Modulo para la huella digital
from machine import UART #importacion de la clase UART del modulo machine
import utime #Importacion de la clase utime

#Declaracion de objetos
AcAlarma = SensoresP()
Msm=SensoresP()
RGB=SensoresP()
ConWifi = SensoresP()
u1=UART(1,57600,tx=22,rx=23)
huella=As608(u1)

#Funcion que envia el mensaje a telegram, Enciende el RGB y activa la alarma
def Prometeo(Estado,Mensaje):
    if Estado==0:
        if ConWifi.conectaWifi ("Familia_Pupo", "Nikol201106"):
            print ("Conexión exitosa!")
            RGB.EncenderRGB(0)
            Msm.EnviarMensaje(Mensaje)
            return True
        else:
            print ("Imposible conectar")
            return False
    else:
        if ConWifi.conectaWifi ("Familia_Pupo", "Nikol201106"):
            print ("Conexión exitosa!")
            RGB.EncenderRGB(1)
            Msm.EnviarMensaje(Mensaje)
            return True
        else:
            print ("Imposible conectar")
            return False

#Valida la huella si esta existe encendera la motocicleta, si no activara la alarma
huella.search() #Valida si la huella exite 
if huella.Encontro==0:
    if Prometeo(0,'Acceso no Autorizado, La alarma se ha activado'):
        AcAlarma.ActivarAlarma()
    else:
        pass
if huella.Encontro==1:
    if Prometeo(1,'Acceso Autorizado'):
       print('')
    else:
        pass
    







