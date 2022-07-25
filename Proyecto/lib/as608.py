from machine import UART
import time, struct, btree

class As608(object):
    def __init__(self,u1):
        self.data0= b'\xef\x01\xff\xff\xff\xff\01\x00\x03\x01\x00\x05'  #
        self.class_all_data = b'\xef\x01\xff\xff\xff\xff\01\x00\x03\x0d\x00\x11'  #
        self.loging_data = b'\xef\x01\xff\xff\xff\xff\01\x00\x03\x10\x00\x14'  #
        self.search_data = b'\xef\x01\xff\xff\xff\xff\01\x00\x03\x11\x00\x15'  #
        self.del_one = b'\xef\x01\xff\xff\xff\xff\01\x00\x07\x0c'  #
        self.u1 = u1

    def del_numid(self,num):
        self.u1.read()
        data = self.del_one + struct.pack ('>h' ,num) + b'\x00\x01'
        data_list = struct.unpack('%db' %len(data[6:]),data[6:])
        data =data+struct.pack('h',sum(data_list))
        self.u1.write(data)
        time.sleep(1)
        rec =self.u1.read()
        if rec[-3:-2] ==b'\x00':
            print('Eliminado %d N°. Huella digital'%num)
            return 1
        else:
            return 0

    def write_btree(self,b_id,b_name):   #
        try:
            f = open("mydb", "r+b")
        except OSError:
            f = open("mydb", "w+b")
        db = btree.open(f)
        db[b_id] = b_name
        db.flush()
        db.close()
        f.close()
    def read_btree(self,b_id):
        try:
            f = open("mydb", "r+b")
        except OSError:
            f = open("mydb", "w+b")
        db=btree.open(f)
        name=db.get(b_id)
        db.close()
        f.close()
        return name
    
    def finger (self): #
        print('Huella detectada')
        self.u1.read()
        self.u1.write(self.data0)
        time.sleep(1)
        rec=self.u1.read()
        if rec[-3:-2] == b'\x00':
            print('Huella detectada')
            return 1
        else:
            return 0
        
    def clear_all(self):
        self.u1.read()
        self.u1.write(self.class_all_data)
        time.sleep(1)
        rec = self.u1.read()
        if rec[-3:-2] == b'\x00':
            print('Todas las huellas han sido borradas')
            import os
            os.remove('mydb')
            return 1
        else:
            return 0
        
    def login(self,into_name=b''):
        ok=self.search()
        print(ok)
        if ok == 0:
            self.u1.read()
            self.u1.write(self.login_data)
            time.sleep(1)
            rec = self.u1.read()
            auth_code=rec[-5:-4]
            if auth_code == b'\x00':
                page_id = rec [-4:-2]
                page_id = struct.unpack('>h',page_id)[0]
                print(page_id)
                self.write_btree(str(page_id),into_name)
                print('Huella registrada correctamente')
                return [1,page_id]
            else:
                print('Registro de huella fallido')
                return 0        
        else:
            print('Esta huella ya ha sido registrada anteriormente')
            
    def search(self):
        self.u1.read()
        self.u1.write(self.search_data)
        time.sleep(1)
        rec=self.u1.read()
        auth_code=rec[-7:-6]
        if auth_code == b'\x00':
            page_id=rec[-6:-4]
            page_id = struct.unpack('>h',page_id)[0]
            score = rec[-4:-2]
            data_btree=self.read_btree(str(page_id))
            print(page_id,score,data_btree)
            return [1,page_id,score,data_btree]
        else:
            print('No se encuentra el registro de la huella')
            return 0
        
if __name__=='__main__':
    u1=UART(1,57600,tx=1,rx=3)
    a=As608(u1)    
    a.finger()    
    id=a.search()
    #a.del_numid(1) #Elimina la huella, colocar el id de la huella
    a.login(name) #Registre nueva huella