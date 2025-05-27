'''
 Un módulo es simplemente un archivo con extensión.py que
 contiene codigo de python(Funciones,clases,variables, etc)

 un paquete es una carpeta que contiene varios módulos,
 (archivos.py) y un archivo especial llamado _init_.py, que le indica a
 python que esa carpeta debe tratarse como un paquete

 '''

import os      
#1.-Funcione que no recibe parametros y no regresa valor

def solicitarDatos1():
    nombre=input("Ingrese su nombre completo: ")
    tel=input("Ingrese su numero celular:")
    print(f"soy la funcion 1 :su nombre es {nombre} y su numero es  {tel}")

solicitarDatos1()
#3.- Funcion que recibe parametros y no regresa valor

def solicitarDatos3(nombre,tel):
   nom=nombre
   telefono=tel

   print(f"Soy la funciones 3: su nombre es {nom} y su numero es  {telefono}")

nombre=input("Ingrese su nombre completo: ")
tel=input("Ingrese su numero celular:")
solicitarDatos3(nombre,tel)

#2.-Funcion que no recibe  parametros y regresa valor

def solicitarDatos2():
    nombre=input("Ingrese su nombre completo: ")
    tel=input("Ingrese su numero celular:")
    return nombre,tel

solicitarDatos2()

#4.- Funcion que recibe parametros y regresa valor

def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel



    return nom,telefono
nombre=input("Ingrese su nombre completo: ")
tel=input("Ingrese su numero celular:")
solicitarDatos4(nombre,tel)

#Mis funciones
solicitarDatos1()

nom3=input("Nombre:")
tel3=input("Tel:")
solicitarDatos3(nom3,tel3)

nom2,tel2=solicitarDatos2()
print(f"Nombre: {nom2} \n Telefono: {tel2}")

nom4=input("Nombre")
telf4=input("Telefono")
nombre4,telefono4=solicitarDatos4(nom4,telf4)

print(f"Nombre:{nombre4} \n Telefono: {telefono4}")

def borrarPantalla():
 os.system("cls")
 
def espereTecla():
   input("...Oprima una tecla para continuar...")

def saludar(nombre):
   nom=nombre
   return f"Hola,bienvenido: {nom}"

