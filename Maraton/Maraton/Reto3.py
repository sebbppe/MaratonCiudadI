import random as rd
from gestionDatos.models import Calle,Carrera,Via,Propietario,Vehiculo,semaforo

class Via():
    def __init__(self,calle,carrera):
        self.calle=calle
        self.carrera=carrera
        
    def setCalle(self,calle):
        self.calle=calle
    def getCalle(self):
        return self.calle
    def setCarrera(self,carrera):
        self.carrera=carrera
    def getCarrera(self):
        return self.carrera
class Propietario():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
    def setApellido(self,apellido):
        self.apellido=apellido
    def getApellido(self):
        return self.apellido
class Vehiculos():
    def __init__(self,tipo,capacidad,placa,propietario):
        self.tipo=tipo
        self.capacidad=capacidad
        self.placa=placa
        self.propietario=propietario
        
    def setTipo(self,tipo):
        self.tipo=tipo
    def getTipo(self):
        return self.tipo
    def setCapacidad(self,capacidad):
        self.capacidad=capacidad
    def getCapacidad(self):
        return self.capacidad
    def setPlaca(self,placa):
        self.placa=placa
    def getPlaca(self):
        return self.placa
    def setPropietario(self,propietario):
        self.propietario=propietario
    def getPropietario(self):
        return self.propietario
class Semaforo():
    def __init__(self,coordenada,estado): 
        self.coordenada=coordenada
        self.estado=estado
        
    def setCoordenada(self,coordenada):
        self.coordenada=coordenada
    def getCoordenada(self):
        return self.coordenada
    def setEstado(self,estado):
        self.estado=estado
    def getEstado(self):
        return self.estado
        
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
bandera=True
while(bandera):
    try:
        calle=int(input("ingrese la cantidad  de calles: "))
        bandera=False
    except:
        print("Error, debe ingresar un número entero")
bandera=True
while(bandera):
    try:
        carrera=int(input("ingrese la cantidad  de carrera: "))
        bandera=False
    except:
        print("Error, debe ingresar un número entero")
bandera=True
while(bandera):
    try:
        habitantes=int(input("ingrese la cantidad de habitantes: "))
        bandera=False
    except:
        print("Error, debe ingresar un número entero")
bandera=True
while(bandera):
    try:
        numVehi=int(input("ingrese la cantitidad de vehículos: "))
        if(numVehi<=int(habitantes*0.2)):
            bandera=False
        else:
            numVehi=int(habitantes*0.2)
            print("Se tomarán  %i vehículos de los ingresados"%numVehi)
            bandera=False
    except:
        print("Error, debe ingresar un número entero")
def generarCalles(call):
    tipoVias=["Calle","Avenida Calle"]
    calles=[]
    ult=0
    for i in range(0,call):
        ale=rd.randint(0,1)
        if(ale==1 and (i-ult>=10)):
            if(ale==0):
                if(i%2==0):
                    calle=Calle(,seccion='Deportes',precio=100000)
                    calles.append([tipoVias[ale]+" "+str(i),"Oriente"])
                else:
                    calles.append([tipoVias[ale]+" "+str(i),"Occidente"])
            else:
                ult=i
                calles.append([tipoVias[ale]+" "+str(i),"Oriente-Occidente"])
        else:
            if(i%2==0):
                calles.append([tipoVias[0]+" "+str(i),"Oriente"])
            else:
                calles.append([tipoVias[0]+" "+str(i),"Occidente"])
    return calles
def generarCarreras(carr):
    tipoVias=["Carrera","Avenida Carrera"]
    carreras=[]
    ult=0
    for i in range(0,carr):
        ale=rd.randint(0,1)
        if(ale==1 and (i-ult>=10)):
            if(ale==0):
                if(i%2==0):
                    carreras.append([tipoVias[ale]+" "+str(i),"Norte"])
                else:
                    carreras.append([tipoVias[ale]+" "+str(i),"Sur"])
            else:
                ult=i
                carreras.append([tipoVias[ale]+" "+str(i),"Norte-Sur"])   
        else:
            if(i%2==0):
                carreras.append([tipoVias[0]+" "+str(i),"Norte"])
            else:
                carreras.append([tipoVias[0]+" "+str(i),"Sur"])
    return carreras
def generarPropietarios(habitantes):
    personas=[]
    for k in range(0,habitantes):
        p=abc[rd.randint(0,25)].upper()
        p1=abc[rd.randint(0,25)].upper()
        nombre=p
        apellido=p1
        for i in range(0,rd.randint(2,4)):
            nombre+=abc[rd.randint(0,25)]
            apellido+=abc[rd.randint(0,25)]
        personas.append([nombre,apellido])
    return personas   
def generarVehiculos(numVehi,personas):        
    vehiculos=[]
    for k in range(0,numVehi):
        placaText=abc[rd.randint(0,25)].upper()+abc[rd.randint(0,25)].upper()+abc[rd.randint(0,25)].upper()
        placaNum=str(rd.randint(0,9))+str(rd.randint(0,9))+str(rd.randint(0,9))
        tipoVehi=["automovil","Camioneta","Camion","buses"]
        tipo=rd.randint(0,3)
        if(tipo==0):
            puestosVehi=5
        elif(tipo==1):
            puestosVehi=7
        elif(tipo==2):
            puestosVehi=3
        elif(tipo==3):
            puestosVehi=rd.randint(20,30)
        tipo=tipoVehi[tipo]
        vehiculos.append([tipo,puestosVehi,placaText+placaNum,personas[rd.randint(0,len(personas)-1)]])
    return vehiculos
def generarSemaforos(via):
    calles=via.getCalle()
    carreras=via.getCarrera()
    semaforos=[]
    ult=[0,0]
    est=["R","A","V","I","FS"]
    for i in range(0,len(calles)):
        for k in range(0,len(carreras)):
            ale=rd.randint(0,1)
            ale2=rd.randint(0,4)
            if(i-ult[0]>=5 and ale==1):
                semaforos.append(Semaforo("Calle "+str(i)+"-Carrera "+str(k),est[ale2]))
                print(i)
                ult=[i,k]
            elif(k-ult[1]>=5 and ale==1):
                semaforos.append(Semaforo("Carrera "+str(k)+"-Calle "+str(i),est[ale2]))
                ult=[i,k]
            else:
                pass
    return semaforos               
vectorCarreras=generarCarreras(carrera)
vectorCalles=generarCarreras(calle)
mallaVial=Via(vectorCalles,vectorCarreras)
vectorPropietarios=generarPropietarios(habitantes)
vectorVehiculos=generarVehiculos(numVehi,vectorPropietarios)
vectorSemaforos=generarSemaforos(mallaVial)

    
    
    
    


art.save()
