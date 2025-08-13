import os
from conexionBD import conexion, cursor
from mysql.connector import Error

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\n\t\t ... Oprima cualquier tecla para continuar ...")

def menu_usuarios():
    print("\n \t..:: Sistema de gestión de libros ::.. \n\t\t1.- Registro \n\t\t2.- Login \n\t\t3.- Salir")
    opcion = input("\t\t Elige una opción: ").strip()
    return opcion

def menu_libreria():
    print("\n \t..:: Menú Librería ::. \n\t1.- Mostrar libros disponibles \n\t2.- Rentar libro \n\t3.- Devolver libro \n\t4.- Mis libros rentados \n\t5.- Salir")
    opcion = input("\t\t Elige una opción: ").strip()
    return opcion

def menu_admin():
    print("\n \t..:: Menú Administrador ::.\n\t1.- Gestionar usuarios\n\t2.- Gestionar libros\n\t3.- Ver reportes de renta\n\t4.- Salir")
    opcion = input("\t\t Elige una opción: ").strip()
    return opcion

def mostrar_libros_rentados(usuario_id):
    try:
        sql = """
        SELECT l.titulo, r.fecha_renta, r.fecha_devolucion_esperada
        FROM rentas r
        JOIN libros l ON r.id_libro = l.id
        WHERE r.id_usuario = %s AND r.fecha_devolucion_real IS NULL
        """
        cursor.execute(sql, (usuario_id,))
        rentados = cursor.fetchall()

        if rentados:
            print(f"{'Titulo':<30}{'Fecha de Renta':<20}{'Fecha Límite':<20}")
            print("-" * 70)
            for titulo, fecha_renta, fecha_limite in rentados:
                print(f"{titulo:<30}{str(fecha_renta):<20}{str(fecha_limite):<20}")
        else:
            print("\t No tienes libros rentados en este momento.")
    except Error as e:
        print(f"Error al mostrar libros rentados: {e}")