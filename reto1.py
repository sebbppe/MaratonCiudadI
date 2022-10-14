import random as rd

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
        bandera=False
    except:
        print("Error, debe ingresar un número entero")

##creamos las vias o mallado vial
tipoVias=["Calle","Avenida Calle","Carrera","Avenida Carrera"]
calles=[]
carreras=[]
for i in range(0,calle):
    calles.append(tipoVias[rd.randint(0,1)]+" "+str(i))
for i in range(0,carrera):
    carreras.append(tipoVias[rd.randint(2,3)]+" "+str(i))

##creamos a las personas
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
    vehiculos.append([tipo,puestosVehi,placaText+placaNum])
    
    
print(calles)
print(carreras)
print(personas)
print(vehiculos)