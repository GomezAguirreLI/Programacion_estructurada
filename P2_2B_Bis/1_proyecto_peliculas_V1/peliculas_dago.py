import os

peliculas=[]
def borrarPantalla():
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print("\n\t.:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre:").upper())
  input("\n\t:::LA OPERACION SE REALIZO CON EXITO:::")

def consultarPeliculas():
  borrarPantalla()
  print(".:: Consultar Peliculas ::.")

  if len(peliculas)>0:
   for i in range(0,len(peliculas)):
     print(f"{i+1}: {peliculas[i]}")
  else:
    print("\n\t..::No hay peliculas en el sistema::..")   

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