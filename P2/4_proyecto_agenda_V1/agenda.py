import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\nIngrese cualquier tecla para continuar:  ")

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\.::Agregar Contacto::..")
    nombre=input("Nombre del Contacto: ").upper().strip()
   
    if nombre in agenda:
        print("\n\t\tEl contácto ya existe...")
    else:
        tel=input("Telefono: ").strip()
        email=input("E-mail: ").lower().strip()
        #Agregar el atributo "nombre" al dict con los valores de tel y email en una lista
        agenda[nombre]=[tel,email]
        print("\n\t\t.::Acción realizada con éxito")

    esperarTecla()

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t.::Mostrar contactos::.")
    if not agenda:
        print("\n\tNo existen contáctos en la Agenda...")
    else:
        for nombre,datos in agenda.items():
            print(f"{'Nombre'+nombre}\n{'Telefono:'+datos[0]}\n{'E-mail:'+datos[1]}")    
    esperarTecla()        


def modificar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nombre==nom:
                print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                tel=input("Ingrese el nuevo numero de telefono: ")
                mail=input("Ingrese el nuevo e-mail: ")
                datos[0]=tel
                datos[1]=mail
                encontro+=1
        if encontro==0:
            print(f"\n\t \u274C No se encontro un contacto con el nombre {nom} para modificar \u274C")

       
        
def eliminar_contacto(agenda):
    borrarPantalla()
    encontro = 0
    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    confirmar = ""
    for nombre, datos in agenda.items():
        if nombre == conta_eliminar:
            print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:' + datos[0]}\n\t{'E-mail:' + datos[1]}")
            while confirmar != "si" and confirmar != "no":
                confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
                if confirmar != "si" and confirmar != "no":
                    print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")
            if confirmar == "si":
                agenda.pop(nombre)
                print(f"\n\t \u2705 El contacto '{nombre}' ha sido eliminado exitosamente. \u2705")
                encontro += 1
    if encontro == 0:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t.::Buscar Contacto::.")
    if not agenda:
        print("\n\t\tNo hay contactos en la agenda.")
    else:
        nombre = input("Ingresa el nombre del contacto que deseas buscar: ").upper().strip()
        encontro = 0
        for n, datos in agenda.items():
            if n == nombre:
                print(f"\n\t{'Nombre: '+n}\n\t{'Telefono: '+datos[0]}\n\t{'E-mail: '+datos[1]}")
                encontro += 1
        if encontro == 0:
            print(f"\n\t \u274C No se encontró un contacto con el nombre {nombre} \u274C")    


def vaciar_agenda(agenda):
    borrarPantalla()
    print("\n\t.:: Borrar o quitar todos los contactos ::.")
    respuesta = input("¿Deseas quitar o borrar todas los contactos del sistema? (si)/(no)").lower()
    if respuesta == "si":
        agenda.clear()
        input("\n\t\t::: \u2705 ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::: \u2705")            