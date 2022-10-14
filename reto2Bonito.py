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
        if(numVehi<=int(habitantes*0.2)):
            bandera=False
        else:
            numVehi=int(habitantes*0.2)
            print("Se tomarán  %i vehículos de los ingresados"%numVehi)
            bandera=False
    except:
        print("Error, debe ingresar un número entero")

##creamos las vias o mallado vial
tipoVias=["Calle","Avenida Calle","Carrera","Avenida Carrera"]
calles=[]
carreras=[]
for i in range(0,calle):
    ale=rd.randint(0,1)
    if(ale==0):
        if(i%2==0):
            calles.append([tipoVias[ale]+" "+str(i),"Oriente"])
        else:
            calles.append([tipoVias[ale]+" "+str(i),"Occidente"])
    else:
        calles.append([tipoVias[ale]+" "+str(i),"Oriente-Occidente"])   
        
for i in range(0,carrera):
    ale=rd.randint(2,3)
    if(ale==2):
        if(i%2==0):
            carreras.append([tipoVias[ale]+" "+str(i),"Norte"])
        else:
            carreras.append([tipoVias[ale]+" "+str(i),"Sur"])
    else:
        carreras.append([tipoVias[ale]+" "+str(i),"Norte-Sur"])        

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
    vehiculos.append([tipo,puestosVehi,placaText+placaNum,personas[rd.randint(0,habitantes-1)]])
    
    

    
print(calles)
print(carreras)
print(personas)

print("Tipo vehículo | Pasajeros | Placa | Propietario")
for vehi in vehiculos:
    print(vehi[0]+"               "+str(vehi[1])+"     "+vehi[2]+"     "+vehi[3][0]+" "+vehi[3][1])