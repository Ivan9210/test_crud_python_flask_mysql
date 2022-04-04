import pymysql

def obtener_conexion():
  try:
      # Cambiar contraseña en atributo password
      conexion = pymysql.connect(host='localhost', user='root', password='root', db='prueba_tecnica')
      
      # OK! conexión exitosa
      print('OK! conexión exitosa')

      return conexion
  except Exception as e:
      # Atrapar error
      print("Ocurrió un error al conectar a SQL Server: ", e)

  

# def obtener_conexion():
#   return pymysql.connect(host='localhost', user='root', password='root', db='prueba_tecnica')