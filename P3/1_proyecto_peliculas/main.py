# Crear un proyeto que permita gestionar (administrar) peliculas, colocar un menu de opciones
# para agregar, eliminar, modificar y consultar peliculas
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar dict para almacenar los siguientes atributos de peliculas (nombre, categoria, clasificacion, genero, idioma)
# 3.- Utilizar e implementar bases de datos


import peliculas

opcion = True
while opcion:
    print(
        "\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- \U0001F4DD Crear  \n\t\t 2.- \U0001F4DB Borrar \n\t\t 3.- \U0001F50D Mostrar \n\t\t 4.- \U0001F501 Modificar \n\t\t 5.- \U0001F6AA Buscar \n\t\t 6.- \U0001F6AA SALIR "
    )
    opcion = input("\t\t\t Elige una opción: ").upper()

    peliculas.borrarPantalla()
    match opcion:
        case "1":
            print(".::\U0001F4DBAgregar Peliculas ::.")
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPantalla()
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.modificarPelicula()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            peliculas.borrarPantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
