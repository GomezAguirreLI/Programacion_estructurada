import funciones
import conexionBD

def main():
    opcion=True
    while opcion:
        funciones.borrarPantallas()
        opcion=funciones.menu_principal()
        if opcion=="1" or opcion=="REGISTRO":
            print("Estoy en opcion 1")
        elif opcion=="2" or opcion=="LOGIN":
            print("Estoy en la opcion 2")
        elif opcion=="3" or opcion=="SALIR":
            print("Termino la ejecuccion del sw")
            funciones.esperarTecla()
            opcion=False
        else:
            print("OPCION NO VALIDA")
            funciones.esperarTecla()            


if __name__ == "__main__":
    main()