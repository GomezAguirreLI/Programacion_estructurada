"""

 dict .-
 Es un tipo de datps que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas
 indices numericos tiene alfanumericos.Es algo parecido como los Objetos


 Tambien se conoce como un arrelgo asosiiativo u objeto json
 el diccionario es una coleccion ordenada y modificable. no hay miembros duplicados
"""
import os
os.system("cls")

#Lista 
#paises=["Mexico","Brazil","Canada","España"]

#dict o objeto
pais_mexico={
        "Nombre":"México",
        "Capital":"CDMX",
        "Población":120000,
        "Idioma":"español",
        "status":True
        }

pais_brasil={

        "Nombre":"Brasil",
        "Capital":"Brasila",
        "Población":10000,
        "Idioma":"portuges",
        "status":True
        }

paises_canada={
        "Nombre":"Canada",
        "Capital":"ottawa",
        "Población":90000,
        "Idioma":["ingles","frances"],
        "status":True
        }

alumno1={
    "nombre":"Daniel",
    "apellido_paterno":"Herndández",
    "apellido_materno":"Goméz",
    "carrera":"TI",
    "area":"Sotware mutiplataforma",
    "modalidad":"Bilingue",
    "matricula":243445,
    "semestre":2
}

#Mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i}={alumno1[i]}")

#Agregar un campo o atributo

alumno1["telefono"]="61821343"

print(alumno1)

""" 
fhand=input("Ingrese una palabra")

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)


"""

palabra=input("Ingrese una palabra")

cuenta=dict()

for i in palabra:
    letras=i.split()
    for letra in letras:
        if letra not in cuenta:
            cuenta[letra]=1
        else:
            cuenta[letra] +=1


bad_word=input("Ingrese una palabra: ").lower()

good_word=bad_word.strip()

print(good_word)




