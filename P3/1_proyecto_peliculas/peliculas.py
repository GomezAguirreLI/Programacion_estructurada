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
    print(f"\n\t[ERROR] No se pudo conectar a la base de datos:")
    print(f"\tDetalles: {e}")
    input("\n\tPresiona ENTER para continuar...")
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
    
    
def mostrarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D ::.\n ")
     cursor=conexionBD.cursor()
     sql="select * from peliculas"
     cursor.execute(sql)
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
     else:
       print("\t .:: \u26A0 No hay peliculas en el sistema \u26A0 ::.") 

def borrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: \U0001F50D Borrar Peliculas \U0001F50D ::.\n ")
        cursor = conexionBD.cursor()
        nombre = input("Dame el nombre de la pelicula a borrar:").upper().strip()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        values = (nombre,)
        cursor.execute(sql, values)
        registros = cursor.fetchall()
        if registros:
            print(f"\nPelícula encontrada:")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print(f"-"*80)
            resp = input(f"Deseas borrar {nombre}? si/no: ").lower().strip()
            if resp == "si":
                sql = "DELETE FROM peliculas WHERE nombre = %s"
                values = (nombre,)
                cursor.execute(sql, values)
                conexionBD.commit()
                print("\n\t\u2705 ¡La película fue borrada exitosamente! \u2705")
        else:
            print("\t .:: \u26A0 La pelicula a buscar no se encuentra \u26A0 ::.")


def buscarPeliculas():
   borrarPantalla()
   conexionBD=conectar()
   if conexionBD!=None:
     print("\n\t.:: \U0001F50D Buscar una Pelicula \U0001F50D ::.\n ")
     cursor=conexionBD.cursor()
     nombre=input("Dame el nombre de la pelicula a buscar:").upper().strip()
     sql="SELECT * FROM peliculas where nombre= %s"
     values=(nombre,)
     cursor.execute(sql, values)
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
         print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)  
     else:
       print("\t .:: \u26A0 La pelicula a buscar no se encuentra \u26A0 ::.") 


def modificarPelicula():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t.:: \U0001F58A Modificar Pelicula \U0001F58A ::.\n ")
        cursor = conexionBD.cursor()
        nombre = input("Dame el nombre de la pelicula a modificar:").upper().strip()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        values = (nombre,)
        cursor.execute(sql, values)
        registro = cursor.fetchone()
        if registro:
            print(f"\nDatos actuales de la película:")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            print(f"{registro[0]:<10}{registro[1]:<15}{registro[2]:<15}{registro[3]:<15}{registro[4]:<15}{registro[5]:<15}")
            print(f"-"*80)
            print("\nDeja vacío el campo si no deseas modificarlo.")
            nuevo_nombre = input(f"Nuevo nombre [{registro[1]}]: ").upper().strip() or registro[1]
            nueva_categoria = input(f"Nueva categoría [{registro[2]}]: ").upper().strip() or registro[2]
            nueva_clasificacion = input(f"Nueva clasificación [{registro[3]}]: ").upper().strip() or registro[3]
            nuevo_genero = input(f"Nuevo género [{registro[4]}]: ").upper().strip() or registro[4]
            nuevo_idioma = input(f"Nuevo idioma [{registro[5]}]: ").upper().strip() or registro[5]
            try:
                sql = """
                UPDATE peliculas SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s WHERE id=%s
                """
                values = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, registro[0])
                cursor.execute(sql, values)
                conexionBD.commit()
                print("\n\t\u2705 ¡La película fue modificada exitosamente! \u2705")
            except Error as e:
                print(f"Error al modificar la película: {e}")
        else:
            print("\t .:: \u26A0 La pelicula a modificar no se encuentra \u26A0 ::.")
