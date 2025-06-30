import os
import platform

empleado={}
empleados=[]
def borrarPantalla():
    #Guardo el nombre del sistema
    sistema=platform.system()
    print(sistema)
    match sistema:

        case "Linux":
            os.system("clear")
        case "Windows":
            os.system("cls")
        case _:
            os.system("clear")
    

def esperarTecla():
    input("\n\t.::Ingrese cualquier tecla para continuar::.")


def agregar_empleado():
    borrarPantalla()
    print("\n\t📝  .:: Alta de Empleado ::.  📝\n ")
    nuevo_empleado = {}
    nuevo_empleado["nombre"] = input("👤 Ingresa el nombre del empleado :").upper()
    nuevo_empleado["edad"] = input("🎂 Ingresa la edad del empleado: ").upper()
    nuevo_empleado["cargo"] = input("💼 Ingresa el cargo del empleado :").upper()
    empleados.append(nuevo_empleado)
    print("\n✅ ..::OPERACIÓN EXITOSA::.. ✅")
    esperarTecla()

def mostrar_empleados():
    borrarPantalla()
    print("\n\t👥  .:: Mostrar empleados guardados ::.  👥\n")
    if len(empleados) > 0:
        for idx, empleado in enumerate(empleados, 1):
            print(f"\n🧑‍💼 Empleado #{idx}:")
            for clave, valor in empleado.items():
                print(f"   • {clave.capitalize()}: {valor}")
        esperarTecla()
    else:
        print("\n🚫 .::NO HAY EMPLEADOS GUARDADOS::. 🚫\n")
        esperarTecla()

def actualizar_empleados():
    borrarPantalla()
    print("\n\t✏️  .:: Modificar características de un empleado ::.  ✏️")
    if len(empleados) > 0:
        for idx, empleado in enumerate(empleados, 1):
            print(f"{idx}. {empleado['nombre']}")
        try:
            seleccion = int(input("\n🔢 Elige el número del empleado a modificar (0 para salir): "))
            if seleccion == 0:
                return
            if 1 <= seleccion <= len(empleados):
                empleado = empleados[seleccion - 1]
                while True:
                    print("\nCaracterísticas actuales:")
                    for i, (clave, valor) in enumerate(empleado.items(), 1):
                        print(f"  {i}. {clave.capitalize()}: {valor}")
                    opcion = int(input("\n✏️  Elige el número de la característica a modificar (0 para salir): "))
                    if opcion == 0:
                        break
                    claves = list(empleado.keys())
                    if 1 <= opcion <= len(claves):
                        clave = claves[opcion - 1]
                        print(f"Valor actual de '{clave.capitalize()}': {empleado[clave]}")
                        nuevo_valor = input(f"Nuevo valor para '{clave.capitalize()}': ").upper()
                        empleado[clave] = nuevo_valor
                        print("\n✅ ..::MODIFICACIÓN EXITOSA::.. ✅\n")
                    else:
                        print("⚠️  Opción inválida. Intenta de nuevo.")
            else:
                print("⚠️  Opción de empleado inválida.")
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.")
        esperarTecla()
    else:
        print("\n🚫 .::NO HAY EMPLEADOS GUARDADOS::. 🚫\n")
        esperarTecla()

def menuEmpleados():
    opcion = True
    while opcion:
        try:
            borrarPantalla()
            print("\n\t👔  .:: Sistema de empleados ::.  👔\n 1️⃣  Agregar empleado\n 2️⃣  Mostrar empleados\n 3️⃣  Modificar empleado\n 4️⃣  Eliminar empleado\n 5️⃣  Salir 🛑")
            opcion = int(input("\n\t👉 Elige una opción: "))
            match opcion:
                case 1:
                    agregar_empleado()
                case 2:
                    mostrar_empleados()
                case 3:
                    actualizar_empleados()
                case 4:
                    eliminar_empleado()
                case 5:
                    print("\n\t👋 ..::SALIENDO DEL SISTEMA DE EMPLEADOS::.. 👋")
                    opcion = False
                case _:
                    print("⚠️  .::Escoje una opción válida::. ⚠️")
                    esperarTecla()
        except ValueError:
            print("⚠️  .::Ingrese un dato numérico::. ⚠️")
            esperarTecla()

def eliminar_empleado():
    borrarPantalla()
    print("\n\t🗑️  .:: Eliminar empleado ::.  🗑️")
    if len(empleados) == 0:
        print("\n🚫 .::NO HAY EMPLEADOS GUARDADOS::. 🚫\n")
        esperarTecla()
        return
    for idx, empleado in enumerate(empleados, 1):
        print(f"{idx}. {empleado['nombre']}")
    try:
        seleccion = int(input("\n🔢 Elige el número del empleado a eliminar (0 para salir): "))
        if seleccion == 0:
            return
        if 1 <= seleccion <= len(empleados):
            confirm = input(f"¿Seguro que deseas eliminar a {empleados[seleccion-1]['nombre']}? (S/N): ").upper()
            if confirm == 'S':
                empleados.pop(seleccion-1)
                print("\n🗑️  ..::EMPLEADO ELIMINADO EXITOSAMENTE::.. 🗑️")
            else:
                print("Operación cancelada.")
        else:
            print("⚠️  Opción inválida.")
    except ValueError:
        print("⚠️  Por favor, ingresa un número válido.")
    esperarTecla()
