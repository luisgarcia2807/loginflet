import psycopg2

def insertar(nombre, apellido, correo, contrasena, pais, tipo_tdah, genero, fecha_nacimiento):
    # Conexión con la base de datos
    conexion = psycopg2.connect(user='postgres',
                                password='password',
                                host='127.0.0.1',
                                port='5432',
                                database='Tdah')  # Nombre de la base de datos 'tdah'

    cursor = conexion.cursor()

    sql = 'INSERT INTO usuario (nombre, apellido, correo, contrasena, pais, tipo_tdah, genero, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    datos = (nombre, apellido, correo, contrasena, pais, tipo_tdah, genero, fecha_nacimiento)
    
    try:
        cursor.execute(sql, datos)
        # Guardar cambios y cerrar conexión
        conexion.commit()
        print("Datos insertados correctamente.")

    except psycopg2.Error as e:
        print(f"Error al insertar datos: {e}")

    finally:
        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()

def mostrar(valor):
    valor= str(valor)
    #conexion con base de datos
    conexion= psycopg2.connect( user= 'postgres',
                               password='password',
                               host='127.0.0.1',
                               port='5432',
                               database='Tdah')
    #para elaborar unas tarea
    cursor=conexion.cursor()

    #sentencia
    sql='SELECT * FROM usuario'
    cursor.execute(sql,(valor,))

    #mostrar
    resgistro=cursor.fetchall()
    

    #cerrar conexion
    cursor.close()
    conexion.close()
    return resgistro

