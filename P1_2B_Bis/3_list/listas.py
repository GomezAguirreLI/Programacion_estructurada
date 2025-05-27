import os
#Ejemplo 1 crear una lista de numeros e imprimir el contenido

num=[1,54,2,54,56,13,7,3,1,5,4,223]

print(num)

for i in num:
    print(i)

for i in range(0,len(num)):
    print(num[i])

#Ejemplo 2 Crear una lista  de palabras y posteriormente buscar la conincidencia de una palabra 
palabras=["Record","Mundial","Estatal","Nacional","Mundial"]

resp="Mundial" in palabras
#1er forma
if resp:
    print("LO ENCONTRE")
    print(f"EL numero de veces que se econtro es : {palabras.count("Mundial")}")
else:
    print("Tsss no salio") 


os.system("cls")
#2da forma
encontro=False
buscar=input("Dame  a buscar: ")
for i in  range(0,len(palabras)):
    if palabras[i]==buscar:
        encontro=True

if encontro:
    print("Si econtre")
else:
    print("No encontro")    


#3da forma 
for i in palabras:
    if i==buscar:
        encontro=True

if encontro:
    print("Si econtre")
else:
    print("No encontro")    



'''
buscar=input("Dame  a buscar la palabra: ")

validacion=True
i=0
while validacion and i<=len(palabras):
    i+=1
    if palabras[i]==buscar:
        print("Encontre la palabra")
        validacion=False
    else:
        print("No encontre la palabra")    

'''

input("Oprima tecla......")       
os.system("cls")

#Añadir elementos a una lista
numeros=[]

opc=True

while opc:
    numero=float(input("Dame un numero entero o decimal: "))
    numeros.append(numero)
    resp=input("¿Deseas  agregar otro numero: ").lower()
    if resp=="si":
        OPC=True
    else:
        opc=False    

print(numeros)

#Ejemplo 4 crear una lista multidimensional que sea una angenda

angeda=[
    ["Carlos","6182334"],
    ["Alberot","652423"],
    ["Martin","8134545"],
    ]

for i in angeda:
    print(i)

input("SSsss")
for r in range(0,3):
    print(angeda[r])
    for c in range(0,2):
        print(angeda[c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{angeda[r][c],}"
        cadena+="\n"

print(cadena)