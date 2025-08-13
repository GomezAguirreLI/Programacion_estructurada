import getpass
import os
from usuarios import usuario
from libros import libro

from rentados import renta
from funciones import (
    borrarPantalla,
    esperarTecla,
    menu_usuarios,
    menu_libreria,
    menu_admin,
    mostrar_libros_rentados,
)

def main():
    while True:
        borrarPantalla()
        opcion = menu_usuarios()
        
        if opcion == "1":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre = input("\t ¿Cual es tu nombre?: ").upper().strip()
            num_telefono = input("\t Ingrese su numero telefonico: ").strip()
            username = input("\t Ingrese un nombre de usuario: ").strip()
            password = getpass.getpass("\t Ingresa tu contraseña: ").strip()
            
            if usuario.registrar(nombre, num_telefono, username, password):
                print(f"\n\t El usuario {nombre}, se registró correctamente.")
            else:
                print(f"\n\t Por favor, inténtelo de nuevo, no fue posible registrar al usuario.")
            esperarTecla()

        elif opcion == "2":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::..")
            username = input("\t Ingrese su nombre de usuario: ").strip()
            password = getpass.getpass("\t Ingrese su contraseña: ").strip()

            user_data = usuario.iniciar_sesion(username, password)
            if user_data:
                if user_data["es_administrador"]:
                    menu_administrador(user_data["nombre"])
                else:
                    menu_libreria_usuario(user_data["id"], user_data["nombre"])
            else:
                print(f"\n\t Usuario y/o contraseña incorrectas, vuelva a intentarlo.")
            esperarTecla()

        elif opcion == "3":
            print("\n\t Hasta luego!")
            break
        
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

def menu_libreria_usuario(usuario_id, nombre):
    while True:
        borrarPantalla()
        print(f"\n\t\t Bienvenid@ {nombre}, ha iniciado sesión con éxito.")
        opcion = menu_libreria()
        
        if opcion == "1":
            borrarPantalla()
            libro.mostrar_libros_disponibles()
            esperarTecla()

        elif opcion == "2":
            borrarPantalla()
            print("\n\t ..:: Rentar Libro ::..")
            renta.rentar_libro(usuario_id)
            esperarTecla()
            
        elif opcion == "3":
            borrarPantalla()
            print("\n\t ..:: Devolver Libro ::..")
            renta.devolver_libro(usuario_id)
            esperarTecla()

        elif opcion == "4":
            borrarPantalla()
            print("\n\t ..:: Mis Libros Rentados ::..")
            mostrar_libros_rentados(usuario_id)
            esperarTecla()

        elif opcion == "5":
            print("\n\t Saliendo del menú de usuario...")
            break
        
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

def menu_administrador(nombre):
    while True:
        borrarPantalla()
   
        

        print(f"\n\t\t Bienvenido Administrador {nombre}, ha iniciado sesión con éxito.")
        opcion = menu_admin()
        
        if opcion == "1":
            borrarPantalla()
            usuario.crud_usuarios()
            esperarTecla()

        elif opcion == "2":
            borrarPantalla()
            libro.crud_libros()
            esperarTecla()
            
        elif opcion == "3":
            borrarPantalla()
            print("\n\t ..:: Reportes ::..")
            renta.mostrar_rentas_activas()
            esperarTecla()

        elif opcion == "4":
            print("\n\t Saliendo del menú de administrador...")
            break
            
        else:
            print("\n\t Opción no válida.")
            esperarTecla()

if __name__ == "__main__":
    main()