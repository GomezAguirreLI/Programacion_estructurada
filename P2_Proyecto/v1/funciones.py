"""
Sistema que maneje la base de datos de una libreria (la del calvario)

vamos a dividir todo por diccionarios, cada libro debe tener: nombre,genero,cantidad de pagina,autor


libro={
    "Nombre":"",
    "Autor":"",
    "Genero":"":,
    "cantidad de paginas":"",
}
"""

import os
#Platform es para ver que sistema se esta usando
import platform



#Pues aca guardamos el libro en si
libro={}
#Y aqui estamos guardando los libros dentro de una lista
libros=[]

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

def menuPrincipal():
    opcion=True
    while opcion:
        try:
            borrarPantalla()
            print("\n\t📚  .:: Sistema informático de una librería ::.  📚\n" +
                  "\n 1️⃣  Agregar libro\n 2️⃣  Mostrar libros\n 3️⃣  Modificar libro\n 4️⃣  Eliminar libro\n 5️⃣  Salir 🛑")
            opcion=int(input("\n	👉 Elige una opción: "))

            match opcion:
                case 1:
                    agregarLibros()
                case 2:
                    mostrarLibros()
                case 3:
                    modificarLibro()
                case 4:
                    eliminarLibro()
                case 5:
                    print("\n\t👋 ..::SALIENDO DEL SW::.. 👋")
                    opcion=False
                case _:
                    print("⚠️  .::Escoje una opción válida::. ⚠️")    
                    esperarTecla()
        except ValueError:
            print("⚠️  .::Ingrese un dato numérico::. ⚠️")
            esperarTecla()


def agregarLibros():
    borrarPantalla()
    print("\n\t📝  .:: Alta de Libros ::.  📝\n ")
    nuevo_libro = {}
    nuevo_libro["nombre"] = input("📖 Ingresa el nombre del libro :").upper()
    nuevo_libro["categoria"] = input("🏷️  Ingresa la categoría del libro: ").upper()
    nuevo_libro["genero"] = input("🎭 Ingresa el género del libro :").upper()
    nuevo_libro["idioma"] = input("🗣️  Ingresa el idioma :").upper()
    nuevo_libro["Cantidad de paginas"] = input("📄 Ingresa la cantidad de páginas del libro: ").upper()
    nuevo_libro["estanteria"] = input("🗄️  Ingresa la estantería donde va a ser guardado :").upper()
    libros.append(nuevo_libro)
    print("\n✅ ..::OPERACIÓN EXITOSA::.. ✅")
    esperarTecla()


def mostrarLibros():
    borrarPantalla()
    print("\n\t📚  .:: Mostrar libros guardados ::.  📚\n")
    if len(libros) > 0:
        for idx, libro in enumerate(libros, 1):
            print(f"\n📗 Libro #{idx}:")
            for clave, valor in libro.items():
                print(f"   • {clave.capitalize()}: {valor}")
        esperarTecla()
    else:
        print("\n🚫 .::NO HAY LIBROS GUARDADOS::. 🚫\n")
        esperarTecla()


def modificarLibro():
    borrarPantalla()
    print("\n\t✏️  .:: Modificar características de un libro ::.  ✏️")
    if len(libros) >0:
        for idx, libro in enumerate(libros, 1):
            print(f"{idx}. {libro['nombre']}")
        try:
            seleccion = int(input("\n🔢 Elige el número del libro a modificar (0 para salir): "))
            if seleccion == 0:
                return
            if 1 <= seleccion <= len(libros):
                libro = libros[seleccion - 1]
                opcion=True
                while opcion:
                    print("\nCaracterísticas actuales:")
                    for i, (clave, valor) in enumerate(libro.items(), 1):
                        print(f"  {i}. {clave.capitalize()}: {valor}")
                    opcion = int(input("\n✏️  Elige el número de la característica a modificar (0 para salir): "))
                    if opcion == 0:
                        opcion=False
                    claves = list(libro.keys())
                    if 1 <= opcion <= len(claves):
                        clave = claves[opcion - 1]
                        print(f"Valor actual de '{clave.capitalize()}': {libro[clave]}")
                        nuevo_valor = input(f"Nuevo valor para '{clave.capitalize()}': ").upper()
                        libro[clave] = nuevo_valor
                        print("\n✅ ..::MODIFICACIÓN EXITOSA::.. ✅\n")
                    else:
                        print("⚠️  Opción inválida. Intenta de nuevo.")
            else:
                print("⚠️  Opción de libro inválida.")
        except ValueError:
            print("⚠️  Por favor, ingresa un número válido.")
        esperarTecla()
    else:
        print("\n🚫 .::NO HAY LIBROS GUARDADOS::. 🚫\n")
        esperarTecla()


def eliminarLibro():
    borrarPantalla()
    print("\n\t🗑️  .:: Eliminar libro ::.  🗑️")
    if len(libros) == 0:
        print("\n🚫 .::NO HAY LIBROS GUARDADOS::. 🚫\n")
        esperarTecla()
        return
    for idx, libro in enumerate(libros, 1):
        print(f"{idx}. {libro['nombre']}")
    try:
        seleccion = int(input("\n🔢 Elige el número del libro a eliminar (0 para salir): "))
        if seleccion == 0:
            return
        if 1 <= seleccion <= len(libros):
            confirm = input(f"¿Seguro que deseas eliminar '{libros[seleccion-1]['nombre']}'? (S/N): ").upper()
            if confirm == 'S':
                libros.pop(seleccion-1)
                print("\n🗑️  ..::LIBRO ELIMINADO EXITOSAMENTE::.. 🗑️")
            else:
                print("Operación cancelada.")
        else:
            print("⚠️  Opción inválida.")
    except ValueError:
        print("⚠️  Por favor, ingresa un número válido.")
    esperarTecla()