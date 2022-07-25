from sensores import SensoresP
from machine import Timer
import utime

#Declaracion de objetos
AcAlarma = SensoresP()
Msm=SensoresP()
RGB=SensoresP()
ConWifi = SensoresP()

def Sonar(Estado):
    if Estado==0:
        if ConWifi.conectaWifi ("Familia_Pupo", "Nikol201106"):
            print ("Conexión exitosa!")
            RGB.EncenderRGB(0)
            Msm.EnviarMensaje("La alarma se a activado")
            return True
        else:
            print ("Imposible conectar")
            return False            

temporiza = Timer(0)
def desborde (Timer):    
    if Sonar(0):
        AcAlarma.ActivarAlarma()
    else:
        print('Se a presentado un error')
    
#______________________
temporiza.init(period=1000,mode=Timer.PERIODIC,callback=desborde)
#_______________________







