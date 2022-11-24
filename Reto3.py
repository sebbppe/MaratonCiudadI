import random as rd

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
    def __init__(self,tipo,capacidad,placa,propietarios):
        self.tipo=tipo
        self.capacidad=capacidad
        self.placa=placa
        self.propietarios=propietarios
        
    def setTipo(self,tipo):
        self.tipo=tipo
    def getNombre(self):
        return self.nombre
    def setApellido(self,apellido):
        self.apellido=apellido
    def getApellido(self):
        return self.apellido
        



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


    
print(generarCarreras(carrera))
