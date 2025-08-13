from conexionBD import conexion, cursor
import hashlib
from mysql.connector import Error
from funciones import esperarTecla, borrarPantalla

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, num_telefono, usuario_nombre, contrasena):
    try:
        contrasena_hash = hash_password(contrasena)
        sql = "INSERT INTO usuarios(nombre, num_telefono, usuario, contrasena, es_administrador) VALUES (%s,%s,%s,%s,%s)"
        val = (nombre, num_telefono, usuario_nombre, contrasena_hash, False)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Error as e:
        print(f"\n\t Error al registrar usuario: {e}")
        return False

def iniciar_sesion(usuario_nombre, contrasena):
    try:
        contrasena_hash = hash_password(contrasena)
        sql = "SELECT id, nombre, es_administrador FROM usuarios WHERE usuario = %s AND contrasena = %s"
        val = (usuario_nombre, contrasena_hash)
        cursor.execute(sql, val)
        registro = cursor.fetchone()

        if registro:
            user_data = {
                "id": registro[0],
                "nombre": registro[1],
                "es_administrador": registro[2]
            }
            return user_data
        else:
            return None
    except Error as e:
        print(f"[ERROR] No se pudo iniciar sesión: {e}")
        return None

def mostrar_todos_los_usuarios():
    try:
        sql = "SELECT id, nombre, num_telefono, usuario, es_administrador FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
        
        if usuarios:
            print("\n\t ..:: Lista de Usuarios ::..")
            print(f"{'ID':<5}{'Nombre':<25}{'Teléfono':<15}{'Usuario':<20}{'Admin':<10}")
            print("-" * 75)
            for fila in usuarios:
                es_admin = "Sí" if fila[4] else "No"
                print(f"{fila[0]:<5}{fila[1]:<25}{fila[2]:<15}{fila[3]:<20}{es_admin:<10}")
        else:
            print("\n\t No hay usuarios registrados.")
    except Error as e:
        print(f"Error al mostrar usuarios: {e}")

def editar_usuario():
    try:
        borrarPantalla()
        mostrar_todos_los_usuarios()
        user_id = int(input("\n\t Ingrese el ID del usuario a editar: ").strip())

        sql_select = "SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(sql_select, (user_id,))
        usuario_a_editar = cursor.fetchone()
        
        if not usuario_a_editar:
            print("\n\t Usuario no encontrado.")
            return

        print(f"\n\t Editando usuario: {usuario_a_editar[1]}")
        nuevo_nombre = input(f"\t Nuevo nombre (actual: {usuario_a_editar[1]}): ").strip() or usuario_a_editar[1]
        nuevo_telefono = input(f"\t Nuevo teléfono (actual: {usuario_a_editar[2]}): ").strip() or usuario_a_editar[2]
        nuevo_usuario = input(f"\t Nuevo usuario (actual: {usuario_a_editar[3]}): ").strip() or usuario_a_editar[3]
        
        es_admin_str = 'Sí' if usuario_a_editar[5] else 'No'
        es_admin_input = input(f"\t ¿Es administrador? (Sí/No, actual: {es_admin_str}): ").strip().lower()
        nuevo_es_admin = True if es_admin_input == 'sí' or es_admin_input == 'si' else False

        sql_update = "UPDATE usuarios SET nombre = %s, num_telefono = %s, usuario = %s, es_administrador = %s WHERE id = %s"
        val = (nuevo_nombre, nuevo_telefono, nuevo_usuario, nuevo_es_admin, user_id)
        cursor.execute(sql_update, val)
        conexion.commit()
        print("\n\t Usuario actualizado con éxito.")

    except Error as e:
        print(f"\n\t Error al editar usuario: {e}")
    except ValueError:
        print("\n\t Por favor, ingrese un ID válido.")

def eliminar_usuario():
    try:
        borrarPantalla()
        mostrar_todos_los_usuarios()
        user_id = int(input("\n\t Ingrese el ID del usuario a eliminar: ").strip())

        if user_id == 1:
            print("\n\t El usuario administrador principal no puede ser eliminado.")
            return

        sql_delete = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql_delete, (user_id,))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print("\n\t Usuario eliminado con éxito.")
        else:
            print("\n\t Usuario no encontrado.")

    except Error as e:
        print(f"\n\t Error al eliminar usuario: {e}")
    except ValueError:
        print("\n\t Por favor, ingrese un ID válido.")

def crud_usuarios():
    while True:
        borrarPantalla()
        print("\n\t ..:: Gestión de Usuarios ::..")
        print("\t 1. Ver todos los usuarios")
        print("\t 2. Editar usuario")
        print("\t 3. Eliminar usuario")
        print("\t 4. Volver al menú de administrador")
        opcion = input("\t Elige una opción: ").strip()
        
        if opcion == "1":
            borrarPantalla()
            mostrar_todos_los_usuarios()
        elif opcion == "2":
            editar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("\n\t Opción no válida.")
        
        if opcion != "4":
            esperarTecla()