
"""
Sets.-
Es un tipo de datos para tener una coleccion de valores pero no tiene ni indicie ni orden

set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.

"""
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
#print(personas)
#personas.pop()
#print(personas)
#personas.clear()
#print(personas)

varios={3.12,3,True,"Hola"}
print(varios)

#EJEMPLO CREAR un programa que solicite los email de los alumnos de la utd almacenar en una lista y posteormente mostrarlo en pantallla sin duplicados
os.system("cls")
opc="si"
email=[]
while opc=="si":
    email.append(input("Dame el email: "))
    opc=input("Deseas solcitar otro email (Si/no): ").lower()

#Imprimir los email sin duplicado


print(email)    
set1=set(email)
print(set1)
email=list(set1)
print(email)