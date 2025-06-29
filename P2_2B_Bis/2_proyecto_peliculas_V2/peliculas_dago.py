import os
#Dict u objeto para almacenar los atributos(nombre,categoria,genero,idioma)



peliculas=[]


#pelicula={
#    "nombre":"",
#    "categoria":"",
#    "genero":"",
#    "idioma":""
#}
pelicula={}


def borrarPantalla():
  os.system("cls")

def esperarTecla():
  input("\n\t.::Oprima cualquier tecla para continuar ::.")
    

def crearPeliculas():
  borrarPantalla()
  print("\n\t.:: Alta de Peliculas ::.\n ")
  pelicula.update({"nombre":input("Ingresa el nombre:").upper()})
  pelicula.update({"categoria":input("Ingresa el categoria:").upper()})
  pelicula.update({"genero":input("Ingresa el genero:").upper()})
  pelicula.update({"idioma":input("Ingresa el idioma:").upper()})


  input("\n\t:::LA OPERACION SE REALIZO CON EXITO:::")

def mostrarPeliculas():
  borrarPantalla()
  print("\n\t.::Consultar o Mostrar la pelicula::.\n")
  if len(pelicula)>0:
    for i in pelicula:
      print(f"\t {i} : {pelicula[i]}")
  else:
    print("\t.::No hay peliculas en el sistema::.")    

def vaciarPeliculas():
  borrarPantalla()
  print("\n\t.::Borrar o quitar todas las peliculas")
  resp=input("¿Deseas quitar o borrar todas las peliculas del sistema (si/no)").lower()

  if resp=="si":
    peliculas.clear()
    input("\n\t:::LA OPERACION SE REALIZO CON EXITO:::")


def buscarPeliculas():
  borrarPantalla()
  print("\n\t..::Buscar una pelicula::..")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  econtro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t ¡No se encuntra la pelicula a buscar")
  else:
    for i in range(0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"La pelicula {pelicula_buscar} si la tenemos y esta y esta en la casilla:{i+1}")
        econtro+=1
      if econtro>0:
        print(f"Tenemos {econtro} peliculas con este titulo")
        input("\n\t:::LA OPERACION SE REALIZO CON EXITO:::")


def eliminarPeliculas():
  buscar=input("Ingrese la pelicula a borrar:").upper()   
  count=0
  existe=buscar in peliculas
  if existe:
    for i in range(0,len(peliculas)):
     if peliculas[i]==buscar:
      resp=input("¿Desea quitar o borrar la pelicula del sistema? (Si/no)").upper().strip()
      if resp=="SI":
        peliculas.remove(buscar)
        print(f" se borró la pelicula {buscar} y estaba en el casillero {i+1}")

        count+=1
      


      if count>0:
        print(f"se borró {count} pelicula(s) con este titulo")                
      else:
        print("..::Lo lamentamos esa pelicula ya fue borrada de la  base de datos::..")
        input("")