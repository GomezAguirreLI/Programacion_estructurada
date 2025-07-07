import os


def limpiarPantalla():
        os.system("cls")

def esperarTecla():
    input("Ingrese una tecla: ")

def agregarPeliculas():
    limpiarPantalla()
    
    
    '''
    print("..::Seccion de agregar peliculas::..")
    pelicula=input("Ingrese la pelicula a añadir a la lista de peliculas: ")
    peliculas.append(pelicula)
    esperarTecla()
       
    '''
    cantidad_pelicuas=int(input("¿Cuantas peliculas desea agregar? "))
    listado_peliculas=[input("Ingresa la pelicula a agregar: ")for i in range(cantidad_pelicuas)]
    return listado_peliculas

def borrarPeliculas(peliculas):

    
    pelicula=input("Ingrese la pelicula a borrar: ")    

    #Busca primero si la pelicula a buscar existe en el la lista 
    existe=pelicula in peliculas

    if existe:
        #Si existe la elimina
        peliculas.remove(pelicula)
        #Esto es solo para visualizar que si se haya borrado es solo temporal
        print(peliculas)
    else:
        #En caso de que la pelicula no exista le avisa al usuario que esta ya fue borrada del programa
        print("..::Lo lamentamos esa pelicula ya fue borrada de la  base de datos::..")

def modificarPeliculas(peliculas):
    #Esta seccion sirve para modificar el nombre de una pelicual en caso de que el usuario se haya equivocado al escribir el nombre en primer lugar
    print(f"En caso de que se haya equivocado aqui puede modificarlo \n\t {peliculas}")
    pelicula_mal_escrita=input("Ingrese la pelicula que usted desea modificar porfavor: ")


    #Verifica que pelicula mal escrita exista ya en la lista de las peliculas
    existe=pelicula_mal_escrita in peliculas

    #Ahora checa lo anterior
    if existe:
         #Como sabemos que si existe vamos a buscar en que posicion esta para poder cambiarla
         for i in range(0,len(peliculas)):
              #por cada posicion de i se pregunta si el contenido de peliculas en la posicion i es igual a la pelicula mal escrita
              if peliculas[i]==pelicula_mal_escrita:
                #Creamos una variable que guarda la pelicula modificada
                pelicula_modificada=input("Ingrese el nombre de la pelicula correcto ")
                peliculas.remove(pelicula_mal_escrita)
                peliculas.insert(i,pelicula_modificada)                 
                print(peliculas)  
    else:
        print("Lo lamentamos la palabra que usted menciona no existe dentro del catalago")


def consultarPeliculas(peliculas):
    #En esta area solo vamos a mostrar al usuario las peliculas que tiene

    for i in range(0,len(peliculas)):
        print(f"\n\t {i+1}.-{peliculas[i]}")

def buscarPeliculas(peliculas):
    #Guardamos la pelicula que el usuario quiere encontrar
    pelicula_buscada=input("Ingrese la pelicula que desea buscar: ")

    #revisamos que exista primero
    existe=pelicula_buscada in peliculas

    if existe:
        #Aqui ya sabemos que existe pero queremos revisar que en donde esta 
        for i in range(0,len(peliculas)):
            if peliculas[i]==pelicula_buscada:
                print(f"La pelicula {pelicula_buscada} esta en el carrete {i+1}")
    else:
        print("Lo lamentamos mucho esa pelicula no esta disponible por el momento....¡le avisaremos cuando este disponible!s")            
    
def vaciarPeliculas(peliculas):
    
    resp=""
    while resp!="si"and resp!="no":
     resp=input("Esta seguro de que desea borrar toda la base de datos de las peliculas?: ").lower()

    if resp=="si":
       peliculas.clear()
            

        
    
       print("listo se borraron todas las peliculas")    