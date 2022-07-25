from machine import Pin,PWM
import utime
import urequests
import network,time


class SensoresP(): #Clase
    def __init__(self): #Metodo constructos
        pass
        
    #para asigar los colores del RGB 
    def Colores(self,a,b,c):
        ledR = Pin(5,Pin.OUT) #Led Rojo
        ledV = Pin(18,Pin.OUT) #Led Verde
        ledA = Pin(4,Pin.OUT) #Led Azul
        ledR(a)
        ledV(b)
        ledA(c)
        
   
    def ActivarAlarma(self): #Metodo de la alarma
        print('alarma activa')
        Alarma=PWM(Pin(32))
        tono=[261, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494]
        while True:
            for i in tono:
                Alarma.freq(i)        
                utime.sleep(0.15)               

    
    def ApagarAlarma(self): #Metodo para apagar la alarma
        print('soy la alarma Apagada')
    
    def EncenderRGB(self,Est): #Metodo del led RGB
        self.Estado=Est
        if self.Estado==0: #No autorizado      
            self.Colores(1,0,0);utime.sleep(2) #Color Rojo
            self.Colores(0,0,0);utime.sleep(2) #Apaga el led
        if self.Estado == 1: #Autorizado
            self.Colores(1,1,0);utime.sleep(2) #Color verde
            self.Colores(0,1,1);utime.sleep(2) #Color Magenta
            self.Colores(0,0,0);utime.sleep(2) #Apaga el led            
    
    def conectaWifi(self,red, password):        
        miRed = network.WLAN(network.STA_IF)     
        if not miRed.isconnected():              #Si no está conectado…
            miRed.active(True)                   #activa la interface
            miRed.connect(red, password)         #Intenta conectar con la red
            print('Conectando a la red', red +"…")
            timeout = time.time ()
            while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
            return True        
    
    def EnviarMensaje(self,Mensaje):
        self.Msm=Mensaje
        bot_token = '5492291306:AAFfFcDNzYPm9T0Xsf2cXGJkwxMCq2Ita_Y'
        bot_chatID = '1502901237'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + self.Msm
        response = urequests.get(send_text)
        print('Mensaje enviado')
        return response.json()
    
    
        
