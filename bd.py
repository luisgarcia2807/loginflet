import qrcode
import psycopg2

def  qr(texto) :
    img= qrcode.make(texto)
    img.save("codigoqrprueba.png")


def mostrar(valor):
    valor= str(valor)
    #conexion con base de datos
    conexion= psycopg2.connect( user= 'postgres',
                               password='password',
                               host='127.0.0.1',
                               port='5432',
                               database='tdah')
    #para elaborar unas tarea
    cursor=conexion.cursor()

    #sentencia
    sql='SELECT * FROM persona where idpersona=(%s)'
    cursor.execute(sql,(valor,))

    #mostrar
    resgistro=cursor.fetchall()
    print(resgistro)

    #cerrar conexion
    cursor.close()
    conexion.close()

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

def modificar(campo,variabledecampo,id):
    #conexion con base de datos
    conexion= psycopg2.connect( user= 'postgres',
                               password='password',
                               host='127.0.0.1',
                               port='5432',
                               database='tdah')
    #para elaborar unas tarea
    cursor=conexion.cursor()
    sql=f'update persona set  {campo} = %s where idpersona= %s'
    data=(variabledecampo,(id,))
    cursor.execute(sql,data)
    conexion.commit()
    #cerrar conexion
    cursor.close()
    conexion.close()

def borrarregistro(id):
    #id = str (id)
   #conexion con base de datos
    conexion= psycopg2.connect( user= 'postgres',
                               password='password',
                               host='127.0.0.1',
                               port='5432',
                               database='tdah')
    #para elaborar unas tarea
    cursor=conexion.cursor()

    sql='DELETE FROM persona where idpersona = %s '
    cursor.execute(sql,(id,))
    conexion.commit()
    print("Su registro fue eliminado")
    cursor.close()
    conexion.close()


#mostrar(15)

#insertar('25','CARLOS',"O-")

#modificar('nombre','PABLO','14')

#borrarregistro(16)


    


