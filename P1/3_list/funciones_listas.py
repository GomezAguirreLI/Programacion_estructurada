"""
List(Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, 
}para acceder a los valores se hace con u indice numerico

Nota: sus valoressi son modificables

la lista es una coleccion ordenada y modificable.
Permite miembros duplicados,
"""
import os
os.system("cls")

#Funciones más comunes en la listas
paises=["México","Brasil","España","Canada"]
numeros=[23,12,100,34]
#Ordenar ascendemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)
#Añadir o Ingresar o Insertar elementos a una lista
#1er forma
paises.append("Honduras")
#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Borrer o Quitar elementos de una lista
#1er forma con el indice
paises.pop(1)
print(paises)
#2da forma con el valor
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
    print("No encontre el pais")    

pais_buscar=input("Dame el pais a buscar: ")
for i in  range(0,len(paises)):
    if paises[i]==pais_buscar:
        print("Si encontre el pais")
    else:
        print("No encontre el pais")    

pais_buscar=input("Dame el pais a buscar: ")

"""validacion=True
i=0
while validacion and i<=len(paises):
    i+=1
    if paises[i]==pais_buscar:
        print("Encontre el pais")
        validacion=False
    else:
        print("No encontre el pais")    

"""

#cuantas veces aparece
print(f"Este numero12 aparece: {numeros.count(12)} veces o veces")

numeros.append(12)
print(f"Este numero12 aparece: {numeros.count(12)} veces o veces")

#Identificar o conocer el indice de un valor 
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de una lista
# 1er forma con los valores 
for i in paises:
    print(i)
#2da forma con los indices
for i in range(0,len(paises)):
     print(f"El valor {i} es: {paises[i]}")    
os.system("cls")
#Unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)

