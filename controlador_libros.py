from base_de_datos import obtener_conexion

# CREATE
def insertar_libro(lib_nombre, lib_descripcion, lib_precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO libros(lib_nombre, lib_descripcion, lib_precio) VALUES (%s, %s, %s)", (lib_nombre, lib_descripcion, lib_precio))
    conexion.commit()
    conexion.close()

# READ
def obtener_libros():
    conexion = obtener_conexion()
    libros = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT lib_id, lib_nombre, lib_descripcion, lib_precio FROM libros")
        libros = cursor.fetchall()
    conexion.close()
    return libros

# READ BY ID
def obtener_libro_por_lib_id(lib_id):
    conexion = obtener_conexion()
    libro = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT lib_id, lib_nombre, lib_descripcion, lib_precio FROM libros WHERE lib_id = %s", (lib_id))
        libro = cursor.fetchone()
    conexion.close()
    return libro

# UPDATE
def actualizar_libro(lib_nombre, lib_descripcion, lib_precio, lib_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE libros SET lib_nombre = %s, lib_descripcion = %s, lib_precio = %s WHERE lib_id = %s", (lib_nombre, lib_descripcion, lib_precio, lib_id))
    conexion.commit()
    conexion.close()

# DELETE
def eliminar_libro(lib_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM libros WHERE lib_id = %s", (lib_id))
    conexion.commit()
    conexion.close()