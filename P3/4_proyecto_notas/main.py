import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t\t {nombre} {apellidos} se registró correctamente con el email: {email}")
            else:
                print(f"\n\t\t ...Por favor intente de nuevo, no fue posible registrar al usuario...")
                
              
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t\t EMAIL O CONTRASEÑA INCORRECTOS, VUELVA A INTENTAR")
                funciones.esperarTecla()
             
            #menu_notas(19,"Dago","Fiscal")
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"Se creo la nota {titulo} exitosamente")
            else:
                print("No fue posible crear la nota en este momento")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=[]
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\tMOSTRAR NOTAS")
                print(f"{'ID':<10} {'ID USUARIO':<15} {'TITULO':<15} {'DESCRIPCION':<15} {'FECHA':<15} ")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10} {fila[1]:<15} {fila[2][:15]:<15} {fila[3][:15]:<15} {fila[4]:<15}")

                print(f"-"*80)
            else:
                print("\t \u26A0 No hay notas en el sistema \u26A0")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas = nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print(f"{'ID':<10} {'ID USUARIO':<15} {'TITULO':<15} {'DESCRIPCION':<15} {'FECHA':<15} ")
                print(f"-"*80)
                for fila in lista_notas:
                    print(f"{fila[0]:<10} {fila[1]:<15} {fila[2][:15]:<15} {fila[3][:15]:<15} {fila[4]:<15}")

                print(f"-"*80)
                funciones.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                id = input("\t \t ID de la nota a actualizar: ")
                titulo = input("\t Nuevo título: ")
                descripcion = input("\t Nueva descripción: ")
                #Agregar codigo

                
                respuesta=nota.cambiar(id,titulo,descripcion)
                if respuesta:
                    print(f"\n\t\t Se actualizo la nota {titulo} exitosamente")
                else:
                    print(f"\n\t\t No fue posible actualizar la nota en este momento")
            else:
                print("NO HAY NOTAS EN EL SISTEMA")
                funciones.esperarTecla(2)
                
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"{'ID':<10} {'ID USUARIO':<15} {'TITULO':<15} {'DESCRIPCION':<15} {'FECHA':<15} ")
            print(f"-"*80)
            for fila in lista_notas:
                print(f"{fila[0]:<10} {fila[1]:<15} {fila[2][:15]:<15} {fila[3][:15]:<15} {fila[4]:<15}")
                print(f"-"*80)
            
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            respuesta=nota.eliminar(id)
            if respuesta:
                print(f"\n\t\t Se borró la nota {id} exitosamente")
            else:
                print(f"\n\t\t No fue posible borrar la nota en este momento")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


