from conexionBD import conexion, cursor
from mysql.connector import Error
from datetime import date, timedelta
from libros import libro

from funciones import esperarTecla

def rentar_libro(id_usuario):
    try:
        libro.mostrar_libros_disponibles()
        esperarTecla()
        id_libro = int(input("Ingresa el ID del libro que deseas rentar: ").strip())
        
        sql_check_renta = "SELECT COUNT(*) FROM rentas WHERE id_usuario = %s AND id_libro = %s AND fecha_devolucion_real IS NULL"
        cursor.execute(sql_check_renta, (id_usuario, id_libro))
        if cursor.fetchone()[0] > 0:
            print("\n\t Ya tienes este libro rentado. Por favor, devuélvelo antes de rentarlo de nuevo.")
            return

        sql_check_stock = "SELECT stock FROM libros WHERE id = %s"
        cursor.execute(sql_check_stock, (id_libro,))
        stock = cursor.fetchone()[0]
        if stock <= 0:
            print("\n\t El libro no está disponible para renta.")
            return

        sql_update_stock = "UPDATE libros SET stock = stock - 1 WHERE id = %s"
        cursor.execute(sql_update_stock, (id_libro,))

        fecha_renta = date.today()
        fecha_devolucion = fecha_renta + timedelta(days=14)
        
        sql_renta = """
            INSERT INTO rentas (id_usuario, id_libro, fecha_renta, fecha_devolucion_esperada)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql_renta, (id_usuario, id_libro, fecha_renta, fecha_devolucion))
        conexion.commit()
        print(f"\n\t Libro rentado con éxito. Debe ser devuelto antes del {fecha_devolucion}.")
    
    except Error as e:
        conexion.rollback()
        print(f"\n\t Error al rentar el libro: {e}")
    except ValueError:
        print("\n\t Por favor, ingresa un ID válido.")

def devolver_libro(id_usuario):
    try:
        print("\n\t Libros que tienes rentados:")
        sql_rentados = """
        SELECT r.id_renta, l.titulo
        FROM rentas r
        JOIN libros l ON r.id_libro = l.id
        WHERE r.id_usuario = %s AND r.fecha_devolucion_real IS NULL
        """
        cursor.execute(sql_rentados, (id_usuario,))
        libros_rentados = cursor.fetchall()
        
        if not libros_rentados:
            print("\n\t No tienes libros para devolver.")
            return

        for renta_id, titulo in libros_rentados:
            print(f"\t ID de Renta: {renta_id} | Título: {titulo}")

        renta_id_a_devolver = int(input("\n\t Ingresa el ID de renta del libro a devolver: ").strip())

        sql_devolver = "UPDATE rentas SET fecha_devolucion_real = %s WHERE id_renta = %s AND id_usuario = %s"
        cursor.execute(sql_devolver, (date.today(), renta_id_a_devolver, id_usuario))

        sql_get_libro_id = "SELECT id_libro FROM rentas WHERE id_renta = %s"
        cursor.execute(sql_get_libro_id, (renta_id_a_devolver,))
        id_libro = cursor.fetchone()[0]

        sql_update_stock = "UPDATE libros SET stock = stock + 1 WHERE id = %s"
        cursor.execute(sql_update_stock, (id_libro,))
        conexion.commit()
        print("\n\t Libro devuelto correctamente.")

    except Error as e:
        conexion.rollback()
        print(f"\n\t Error al devolver el libro: {e}")
    except ValueError:
        print("\n\t Por favor, ingresa un ID de renta válido.")

def mostrar_rentas_activas():
    try:
        sql = """
        SELECT r.id_renta, u.nombre AS usuario, l.titulo AS libro, r.fecha_renta, r.fecha_devolucion_esperada
        FROM rentas r
        JOIN usuarios u ON r.id_usuario = u.id
        JOIN libros l ON r.id_libro = l.id
        WHERE r.fecha_devolucion_real IS NULL
        """
        cursor.execute(sql)
        rentas_activas = cursor.fetchall()

        if rentas_activas:
            print("\n\t ..:: Reporte de Rentas Activas ::..")
            print(f"{'ID Renta':<10}{'Usuario':<25}{'Libro':<30}{'Fecha Renta':<15}{'Fecha Límite':<15}")
            print("-" * 95)
            for renta_id, usuario, libro, fecha_renta, fecha_limite in rentas_activas:
                print(f"{renta_id:<10}{usuario:<25}{libro:<30}{str(fecha_renta):<15}{str(fecha_limite):<15}")
            
           

        else:
            print("\n\t No hay libros rentados en este momento.")
    except Error as e:
        print(f"Error al generar reporte de rentas: {e}")