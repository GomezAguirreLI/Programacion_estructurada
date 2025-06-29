'''
Crear un proyecto, que permita gestionar(administrar) peliculas, colocar un menu de opciones para agregar,eliminar,modificar y consultar peliculas.

Notas:
1.-Utilizar funciones y mandar a llamar desde otro archivo.
2.-Utilizara listas para almacenar los nombres de peliculas.

'''
import peliculass

peliculass.limpiarPantalla
print("..::Sistema informatico del cine punto guadiana::..")
peliculass.esperarTecla()
opcion=0
peliculas=[]

ejecucion=True
while ejecucion:
    try:
        peliculass.limpiarPantalla()
        opcion=int(input("\n\t..::Menu de opciones::..\n\t Ingrese un numero para poder escoger una opcion \n\t 1.-Agregar \n\t 2.-Eliminar \n\t 3.-Modficar \n\t 4.-Consultar \n\t 5.-Buscar peliculas \n\t 6.-Vaciar peliculas \n\t 7.-Salir \n\t :"))
   
        match opcion:
            case 1:
                peliculas=peliculass.agregarPeliculas()

            case 2:
                peliculass.limpiarPantalla()
                print("..::Borra Pelicula::..")
                peliculass.borrarPeliculas(peliculas)
                peliculass.esperarTecla()
            case 3:
                peliculass.limpiarPantalla()
                print("..::Modificar Peliculas::..")
                peliculass.modificarPeliculas(peliculas)
                peliculass.esperarTecla()
            case 4:
                peliculass.limpiarPantalla()
                print("..::Consultar Pelicula::..")
                peliculass.consultarPeliculas(peliculas)

                peliculass.esperarTecla()
            case 7:
                peliculass.limpiarPantalla()
                print("..::Salir del programa")
                peliculass.esperarTecla()
                ejecucion=False
                opcion=6 
            case 6:
                peliculass.limpiarPantalla()
                print("..::Vaciar peliculas::..")
                peliculass.vaciarPeliculas(peliculas)
                
                peliculass.esperarTecla()
            case 5:
                peliculass.limpiarPantalla()
                print("..::Buscar peliculas::..")
                peliculass.buscarPeliculas(peliculas)
                peliculass.esperarTecla()          
            case _:
                print("Opcion no valida intente de nuevo")
                peliculass.esperarTecla()
    except ValueError:
        print("Disculpe, intente solo digitar numeros.")
        peliculass.esperarTecla()
        peliculass.limpiarPantalla()
