"""
Este es la pagina principal
"""


import funciones
import empleados

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        print("\n\t✨  .:: SISTEMA PRINCIPAL ::.  ✨\n" +
              "\n 1️⃣  Menú de Libros\n 2️⃣  Menú de Empleados\n 3️⃣  Salir 🛑")
        try:
            opcion = int(input("\n\t👉 Elige una opción: "))
            match opcion:
                case 1:
                    funciones.menuPrincipal()
                case 2:
                    empleados.menuEmpleados()
                case 3:
                    print("\n\t👋 ..::SALIENDO DEL SISTEMA::.. 👋")
                    opcion=False
                case _:
                    print("⚠️  .::Escoje una opción válida::. ⚠️")
                    funciones.esperarTecla()
        except ValueError:
            print("⚠️  .::Ingrese un dato numérico::. ⚠️")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()