import sqlite3



# Conexión a la base de datos (crea la base de datos si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER
    )
''')

# Función para insertar un nuevo usuario
def crear_usuario(nombre, edad):
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, edad))
    conn.commit()
    print(f'Se ha creado el usuario {nombre} de {edad} años.')

# Función para leer todos los usuarios
def obtener_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

# Función para actualizar la edad de un usuario por su ID
def actualizar_usuario(id_usuario, nueva_edad):
    cursor.execute('UPDATE usuarios SET edad = ? WHERE id = ?', (nueva_edad, id_usuario))
    conn.commit()
    print(f'Se ha actualizado la edad del usuario con ID {id_usuario}.')

# Función para eliminar un usuario por su ID
def eliminar_usuario(id_usuario):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_usuario,))
    conn.commit()
    print(f'Se ha eliminado el usuario con ID {id_usuario}.')

# Ejemplo de uso
crear_usuario('Juan', 25)
crear_usuario('María', 30)

print('Usuarios antes de la actualización:')
obtener_usuarios()

actualizar_usuario(1, 26)

print('Usuarios después de la actualización:')
obtener_usuarios()

eliminar_usuario(2)

print('Usuarios después de la eliminación:')
obtener_usuarios()

# Cerrar la conexión a la base de datos
conn.close()
