#Proyecto 1
#Crear un proyecto que permita administrar peliculas, colocar un menu de opciones para agregar, eliminar, modificar y agregar
#Usar base de datos para gestionar peliculas

import peliculas

opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Modificar \n\t\t 5.- Buscar Pelicula \n\t\t 6.- SALIR "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()

    peliculas.borrarpantalla()
    match opcion:
        case "1":
            print(".:: Agregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarPeliculas()
            input("Oprima cualquier tecla para continuar ...")
        case "4":
            peliculas.modificarpelicula1()
            peliculas.esperartecla()
        case "5":
            peliculas.buscarpeliculas()
            peliculas.esperartecla
        case "6":
            opcion = False
            peliculas.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            peliculas.borrarpantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")