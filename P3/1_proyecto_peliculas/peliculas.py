import mysql.connector
from mysql.connector import Error

#DICT U OBJETO para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

#            "nombre":"",
#           "categoria":"",
#            "clasificacion":"",
#            "genero":"idioma",
#            }

pelicula={}
def borrarpantalla():
    import os
    os.system("cls")


def esperartecla():
    input("\t Oprima cualquier tecla para continuar ...")
    borrarpantalla()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"EL ERROR QUE SUCEDIÓ FUE: {e}")
        return None

def crearPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.::\U0001F4DD Alta de Peliculas \U0001F4DD::. ")
        pelicula.update({"nombre":input("Ingresa el nombre: ".upper().strip())}) 
        pelicula.update({"categoria":input("Ingresa la categoria: ".upper().strip())}) 
        pelicula.update({"clasificacion":input("Ingresa la clasificacion: ".upper().strip())}) 
        pelicula.update({"genero":input("Ingresa el genero: ".upper().strip())}) 
        pelicula.update({"idioma":input("Ingresa el idioma: ".upper().strip())}) 
        
        #### AGREGAR REGISTRO A LA BASE DE DATOS

        try:
            cursor=conexion.cursor()
            sql="INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
            val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"], pelicula["idioma"])
            cursor.execute(sql,val)
            conexion.commit()
            input("\n\t\t :::\u2705 LA OPERACION SE REALIZO CON EXITO! \u2705:::")     
        except Error as e:
            input("\n\t\t :::\u2705 ERROR AL INSERTAR REGISTRO \u2705:::")     
  
       

                     
def mostrarPeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        sql="SELECT * FROM peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\tMOSTRAR PELICULAS")
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [1]:<15} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15} ")
            print(f"-"*80)
        else:
            print("\t \u26A0 No hay peliculas en el sistema \u26A0")

def buscarpeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        sql="SELECT * FROM peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\n\tMOSTRAR PELICULAS")
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15}")
            print(f"-"*80)
        else:
            print("\t \u26A0 No hay peliculas en el sistema \u26A0")

def agregarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t .:: \U0001F4DD Agregar Caracteristica a Peliculas \U0001F4DD::.\n")
    atributo=input("Ingresa la nueva caracteristica de la Pelicula: ").lower().strip()
    valor=input("\U0001F4DD Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula.update({atributo:valor})

def buscarpeliculas():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Consultar o Mostrar la Pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a buscar")
        sql="SELECT * FROM peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\n\tMOSTRAR PELICULAS")
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [1]:<15} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15} ")
            print(f"-"*80)
        else:
            print("\t \u26A0 No hay peliculas en el sistema \u26A0")
            
          
def modificarPelicula():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Borrar una pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a modificar")
        sql="SELECT * FROM peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [1]:<15} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15} ")
            print(f"-"*80)
            resp=input(f"¿Deseas modificar {nombre} SI/NO").lower().strip()
            if resp=="si":
                pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
                pelicula["categoria"]=input("Ingresa la categoria: ").upper().strip()
                pelicula["clasificacion"]=input("Ingresa la clasificacion: ").upper().strip()
                pelicula["genero"]=input("Ingresa el genero: ").upper().strip() 
                pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip() 
                sql="UPDATE peliculas SET nombre=%s,categoria=%s,clasificacion=%s,genero=%s, idioma=%s WHERE nombre=%s"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
                cursor.execute(sql,val)
                conexion.commit()
                print("\t \u26A0 Accion realizaa con exito \u26A0")
            else:
                print("\t \u26A0 No hay peliculas en el sistema \u26A0")
                
def borrarPelicula():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Borrar una pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a borrar")
        sql="SELECT * FROM peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [1]:<15} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15} ")
            print(f"-"*80)
            resp=input(f"¿Deseas borrar {nombre} SI/NO").lower().strip()
            if resp=="si":
                sql="DELETE FROM peliculas WHERE nombre=%s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexion.commit()
                print("\t \u26A0 Accion realizada con exito \u26A0")
            else:
                print("\t \u26A0 No hay peliculas en el sistema \u26A0")
                
def modificarpelicula1():
    borrarpantalla()
    conexion=conectar()
    if conexion!=None:
        print("\n\t.:: \U0001F50D Modificar una pelicula \U0001F50D::. \n")
        cursor=conexion.cursor()
        nombre=input("Dame el nombre de la pelicula a modificar")
        sql="SELECT * FROM peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':<10} {'NOMBRE':<15} {'CATEGORIA':<15} {'CLASIFICACION':<15} {'GENERO':<15} {'IDIOMA':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila [0]:<10} {fila [1]:<15} {fila [2]:<15} {fila [3]:<15} {fila [4]:<15} {fila [5]:<15} ")
            print(f"-"*80)
            resp=input(f"¿Deseas modificar {nombre} SI/NO").lower().strip()
            if resp=="si":
                pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
                pelicula["categoria"]=input("Ingresa la categoria: ").upper().strip()
                pelicula["clasificacion"]=input("Ingresa la clasificacion: ").upper().strip()
                pelicula["genero"]=input("Ingresa el genero: ").upper().strip() 
                pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip() 
                sql="UPDATE peliculas SET nombre=%s,categoria=%s,clasificacion=%s,genero=%s, idioma=%s WHERE nombre=%s"
                val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
                cursor.execute(sql,val,pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
                conexion.commit()
                print("\t \u26A0 Accion realizada con exito \u26A0")
            else:
                print("\t \u26A0 No hay peliculas en el sistema \u26A0")