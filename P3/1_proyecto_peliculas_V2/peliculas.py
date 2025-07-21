import mysql.connector
from mysql.connector import Error

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

# pelicula={
#             "nombre":"",
#             "categoria":"",
#             "clasificacion":"",
#             "genero":"",
#             "idioma":""
#           }

pelicula={}

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠ Oprima cualquier tecla para continuar ⚠ ...")

def conectar():
  try:
      conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"
      )
      return conexion
  except Error as e:
    print(f"El erro que sucedio es: {e}")
    return None



def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: \U0001F4DD Alta de Peliculas \U0001F4DD ::.\n ")
    # pelicula['nombre']=input("\U0001F4DD nombre: ").upper().strip()
    pelicula.update({"nombre":input("\U0001F4DD nombre: ").upper().strip()})
    pelicula.update({"categoria":input("\U0001F4DD categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input("\U0001F4DD clasificación: ").upper().strip()})
    pelicula.update({"genero":input("\U0001F4DD genero: ").upper().strip()})
    pelicula.update({"idioma":input("\U0001F4DD idioma: ").upper().strip()})

    ###### AGREGAR REGISTRO A LA BD
    try:
      cursor=conexionBD.cursor()
      sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) values (%s,%s,%s,%s,%s)"
      val=(pelicula['nombre'],pelicula['categoria'],pelicula['clasificacion'],pelicula['genero'],pelicula['idioma'])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t\t ::: \u2705 ¡LA OPERACION SE REALIZO CON EXÍTO! \u2705 :::")
    except Error as e:
      print(f"Error al intentar insertar un registro en la BD: {e}")
    
    
def buscarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Buscar  Pelicula \U0001F50D ::.\n ")
     nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
     cursor=conexionBD.cursor()
     sql="SELECT * FROM peliculas WHERE nombre=%s"
     val=(nombre,)
     cursor.execute(sql,val)
     #fetchall regresa todos los valores que sean iguales pero fetchone solo saca un valor
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<25}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
       input("presione cualquier tecla para continuar")
     else:
       print("\t .:: \u26A0 Esta pelicula/s no se encuentra \u26A0 ::.") 

   
def borrarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Buscar  Pelicula \U0001F50D ::.\n ")
     nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
     cursor=conexionBD.cursor()
     sql="SELECT * FROM peliculas WHERE nombre=%s"
     val=(nombre,)
     cursor.execute(sql,val)
     #fetchall regresa todos los valores que sean iguales pero fetchone solo saca un valor
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<25}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
       resp=input(f"Deseas borrar la pelicula de nombre {nombre}? (si/no)").lower().strip()
       if resp=="si":
         sql="DELETE from peliculas WHERE nombre=%s"
         val=(nombre,)
         cursor.execute(sql,val)
         #si esta no se ejecuta se cancela la linea anterior
         conexionBD.commit()
         print(f"La pelicula {nombre} ha sido borrada correctamente del proyecto")
     else:
       print("\t .:: \u26A0 Esta pelicula/s no se encuentra \u26A0 ::.") 


def mostrarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Buscar  Pelicula \U0001F50D ::.\n ")
     cursor=conexionBD.cursor()
     sql="SELECT * FROM peliculas"
     
     cursor.execute(sql)
     #fetchall regresa todos los valores que sean iguales pero fetchone solo saca un valor
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<25}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
       input("presione cualquier tecla para continuar")
     else:
       print("\t .:: \u26A0 Esta pelicula/s no se encuentra \u26A0 ::.") 

def modificarPeliculas():
  '''
  si hay dos peliculas o n peliculas que se llamen igual 
  '''

  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: \U0001F50D Buscar  Pelicula \U0001F50D ::.\n ")
    nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="SELECT * FROM peliculas WHERE nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    #fetchall regresa todos los valores que sean iguales pero fetchone solo saca un valor
    registros=cursor.fetchall()
    if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<25}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<25}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
        resp=input(f"Deseas modifcar la pelicula de nombre {nombre}? (si/no)").lower().strip()
        if resp=="si":
          pelicula['nombre']=input("\U0001F4DD nombre: ").upper().strip()
          pelicula["categoria"]=input("\U0001F4DD categoría: ").upper().strip()
          pelicula["clasificacion"]=input("\U0001F4DD clasificación: ").upper().strip()
          pelicula["genero"]=input("\U0001F4DD genero: ").upper().strip()
          pelicula["idioma"]=input("\U0001F4DD idioma: ").upper().strip()

          sql="update peliculas  set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s where nombre=%s"
          val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
          cursor.execute(sql,val)
          #si esta no se ejecuta se cancela la linea anterior
          conexionBD.commit()
          print(f"La pelicula {nombre} ha sido modificada correctamente del proyecto")

    else:
       print("\t .:: \u26A0 Esta pelicula/s no se encuentra \u26A0 ::.") 