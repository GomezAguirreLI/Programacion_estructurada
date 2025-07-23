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
            print("\n \t 📝 ..:: Registro en el Sistema ::.. 📝")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente con el email: {email}")
            else:
                print(f"\n\t Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t 🔑 ..:: Inicio de Sesión ::.. 🔑")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            registro=usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas, vuelva a intentarlo")
                funciones.esperarTecla() 
              
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
        print(f"\n \t \t \t 👋 Bienvenido {nombre} {apellidos}, has iniciado sesión ... 👋")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t 🆕 .:: Crear Nota ::. 🆕")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta:
                print(f"\n\t ✅ Se creó la nota: {titulo} exitosamente ✅")
            else:
                print("\n\t ❌ No fue posible crear la nota en este momento, vuelve a intentar... ❌")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\t 📋 Mostrar las Notas 📋")
                print(f"{'ID':>15}{'Titulo':>20}{'Descripcion':>20}{'Fecha':>20}")
                for fila in lista_notas:
                    print("-"*90)
                    # Formatear la fecha si es datetime
                    fecha = fila[4]
                    if hasattr(fecha, 'strftime'):
                        fecha_str = fecha.strftime('%d/%m/%Y')
                    else:
                        fecha_str = str(fecha)
                    print(f"{fila[0]:>15}{fila[2]:>20}{fila[3]:>20}{fecha_str:>20}")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t ✏️ .:: {nombre} {apellidos}, vamos a modificar una Nota ::. ✏️ \n")
           #Muestra las notas
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                print("\n\t 📋 Mostrar las Notas 📋")
                print(f"{'ID':>15}{'Titulo':>20}{'Descripcion':>20}{'Fecha':>20}")
                for fila in lista_notas:
                    print("-"*90)
                    # Formatear la fecha si es datetime
                    fecha = fila[4]
                    if hasattr(fecha, 'strftime'):
                        fecha_str = fecha.strftime('%d/%m/%Y')
                    else:
                        fecha_str = str(fecha)
                    print(f"{fila[0]:>15}{fila[2]:>20}{fila[3]:>20}{fecha_str:>20}")
                    print(f"{'/'*100}")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")



            existe = False
            while not existe:
                id = input("\t \t ID de la nota a actualizar: ")
                existe = any(str(fila[0]) == id for fila in lista_notas)
                if not existe:
                    print("Intente de nuevo ya que el id que puso no está en notas")

            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")

            
            
            resp=input(f"¿Esta seguro de que quiere modificar la nota {id} ?(Y/N):  ").upper().strip()
            if resp=="Y":
                #Agregar codigo
                respuesta=nota.cambiar(id,titulo,descripcion)
                if respuesta:
                    print(f"\n\t ✅ Se actualizó la nota: {titulo} exitosamente ✅")
                else:
                    print("\n\t ❌ No fue posible actualizar la nota en este momento, vuelve a intentar... ❌")
            else:
                pass
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t 🗑️ .:: {nombre} {apellidos}, vamos a borrar una Nota ::. 🗑️ \n")
            flag=False
            #Agregar codigoz
            #Muestra las notas que ya existen
            lista_notas=nota.mostrar(usuario_id)
            if len(lista_notas)>0:
                flag=True

                print("\n\t 📋 Notas 📋")
                print(f"{'ID':>15}{'Titulo':>20}{'Descripcion':>20}{'Fecha':>20}")
                for fila in lista_notas:
                    print("-"*90)
                    # Formatear la fecha si es datetime
                    fecha = fila[4]
                    if hasattr(fecha, 'strftime'):
                        fecha_str = fecha.strftime('%d/%m/%Y')
                    else:
                        fecha_str = str(fecha)
                    print(f"{fila[0]:>15}{fila[2]:>20}{fila[3]:>20}{fecha_str:>20}")
                    print(f"{'/'*100}")
            else:
                print(f"\n\t No existen notas de acuerdo al usuario")


            if flag:
                flag=False

                existe = False
                while not existe:
                 id = input("\t \t ID de la nota a borrar: ")
                 flag=True
                 existe = any(str(fila[0]) == id for fila in lista_notas)
                 if not existe:
                    print("Intente de nuevo ya que el id que puso no está en notas")

                

                if flag:
                    resp=input(f"¿Esta seguro de que quiere borrar la nota {id} ?(Y/N):  ").upper().strip()
                    if resp=="Y":
                        respuesta=nota.borrar(id)
                        if respuesta:
                            print(f"\n\t ✅ Se borró la nota: {id} exitosamente ✅")
                        else:
                            print("\n\t ❌ No fue posible borrar la nota en este momento, vuelve a intentar... ❌") 
                    else:
                        pass               
                funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()