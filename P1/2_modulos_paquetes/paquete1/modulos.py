import os
def borrarPantalla():
 os.system("cls")
 
def espereTecla():
   input("...Oprima una tecla para continuar...")

def saludar(nombre):
   nom=nombre
   return f"Hola,bienvenido: {nom}"


def solicitarDatos2():
    nombre=input("Ingrese su nombre completo: ")
    tel=input("Ingrese su numero celular:")
    return nombre,tel
