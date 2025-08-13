from conexionBD import conexion, cursor
from mysql.connector import Error
from funciones import esperarTecla, borrarPantalla

def crear_libro():
    try:
        borrarPantalla()
        print("\n\t ..:: Crear Nuevo Libro ::..")
        titulo = input("Ingresa el título del libro: ").strip()
        autor = input("Ingresa el nombre del autor: ").strip()
        categoria = input("Ingresa la categoría del libro: ").strip()
        idioma = input("Ingresa el idioma del libro: ").strip()
        paginas = int(input("Ingresa la cantidad de páginas del libro: ").strip())
        estanteria = input("Ingresa la estantería: ").strip()
        stock = int(input("Ingresa el número de copias (stock): ").strip())

        sql = """
            INSERT INTO libros (titulo, autor, categoria, idioma, cant_paginas, estanteria, stock)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        val = (titulo, autor, categoria, idioma, paginas, estanteria, stock)
        cursor.execute(sql, val)
        conexion.commit()
        print("\n\t\t ::: Libro agregado con éxito! :::")
    except Error as e:
        print(f"\n\t\t ::: Error al agregar el libro: {e} :::")
    except ValueError:
        print("\n\t\t ::: Error: Cantidad de páginas y stock deben ser números enteros. :::")

def mostrar_libros_disponibles():
    try:
        borrarPantalla()
        sql = "SELECT id, titulo, autor, categoria, estanteria, stock FROM libros"
        cursor.execute(sql)
        libros = cursor.fetchall()
        
        if libros:
            print("\n\t ..:: Libros disponibles ::..")
            print(f"{'ID':<5}{'Titulo':<30}{'Autor':<25}{'Categoría':<20}{'Estantería':<15}{'Stock':<10}")
            print("-" * 105)
            for fila in libros:
                print(f"{fila[0]:<5}{fila[1]:<30}{fila[2]:<25}{fila[3]:<20}{fila[4]:<15}{fila[5]:<10}")
        else:
            print("\n\t No hay libros disponibles en este momento.")
    except Error as e:
        print(f"Error al mostrar libros: {e}")

def editar_libro():
    try:
        mostrar_libros_disponibles()
        libro_id = int(input("\n\t Ingrese el ID del libro a editar: ").strip())

        sql_select = "SELECT * FROM libros WHERE id = %s"
        cursor.execute(sql_select, (libro_id,))
        libro_a_editar = cursor.fetchone()
        
        if not libro_a_editar:
            print("\n\t Libro no encontrado.")
            return

        print(f"\n\t Editando libro: {libro_a_editar[1]}")
        nuevo_titulo = input(f"\t Nuevo título (actual: {libro_a_editar[1]}): ").strip() or libro_a_editar[1]
        nuevo_autor = input(f"\t Nuevo autor (actual: {libro_a_editar[2]}): ").strip() or libro_a_editar[2]
        nueva_categoria = input(f"\t Nueva categoría (actual: {libro_a_editar[3]}): ").strip() or libro_a_editar[3]
        nuevo_idioma = input(f"\t Nuevo idioma (actual: {libro_a_editar[4]}): ").strip() or libro_a_editar[4]
        
        # Manejo de valores numéricos para páginas y stock
        try:
            nuevas_paginas = int(input(f"\t Nueva cantidad de páginas (actual: {libro_a_editar[5]}): ").strip() or libro_a_editar[5])
        except ValueError:
            nuevas_paginas = libro_a_editar[5]

        nuevo_estanteria = input(f"\t Nueva estantería (actual: {libro_a_editar[6]}): ").strip() or libro_a_editar[6]

        try:
            nuevo_stock = int(input(f"\t Nuevo stock (actual: {libro_a_editar[7]}): ").strip() or libro_a_editar[7])
        except ValueError:
            nuevo_stock = libro_a_editar[7]

        sql_update = """
            UPDATE libros 
            SET titulo = %s, autor = %s, categoria = %s, idioma = %s, cant_paginas = %s, estanteria = %s, stock = %s 
            WHERE id = %s
        """
        val = (nuevo_titulo, nuevo_autor, nueva_categoria, nuevo_idioma, nuevas_paginas, nuevo_estanteria, nuevo_stock, libro_id)
        cursor.execute(sql_update, val)
        conexion.commit()
        print("\n\t Libro actualizado con éxito.")

    except Error as e:
        print(f"\n\t Error al editar libro: {e}")
    except ValueError:
        print("\n\t Por favor, ingrese un ID válido.")

def eliminar_libro():
    try:
        mostrar_libros_disponibles()
        libro_id = int(input("\n\t Ingrese el ID del libro a eliminar: ").strip())

        sql_delete = "DELETE FROM libros WHERE id = %s"
        cursor.execute(sql_delete, (libro_id,))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print("\n\t Libro eliminado con éxito.")
        else:
            print("\n\t Libro no encontrado.")

    except Error as e:
        print(f"\n\t Error al eliminar libro: {e}")
    except ValueError:
        print("\n\t Por favor, ingrese un ID válido.")

def crud_libros():
    while True:
        borrarPantalla()
        print("\n\t ..:: Gestión de Libros ::..")
        print("\t 1. Crear nuevo libro")
        print("\t 2. Mostrar libros disponibles")
        print("\t 3. Editar libro existente")
        print("\t 4. Eliminar libro")
        print("\t 5. Volver al menú de administrador")
        opcion = input("\t Elige una opción: ").strip()

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            mostrar_libros_disponibles()
        elif opcion == "3":
            editar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            break
        else:
            print("\n\t Opción no válida.")
        
        if opcion != "5":
            esperarTecla()