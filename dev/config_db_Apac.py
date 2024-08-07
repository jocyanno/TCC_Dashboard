import mysql.connector
from load_env import db_host, db_password, db_port, db_user, db_database_apac

def create_connection_tendencia_APAC():
  
  connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database_apac,
    port=db_port
  )

  return connection

def consultar_ultimo_registro_tendencia():
  connection = create_connection_tendencia_APAC()
  cursor = connection.cursor()
  query = """
  SELECT * FROM tendencia 
  ORDER BY id DESC 
  LIMIT 5
  """
  cursor.execute(query)
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  return result

def consultar_ultimo_registro_tendencia_grafico():
    connection = create_connection_tendencia_APAC()
    cursor = connection.cursor()
    query = """
    SELECT data, metropolitana, min, max 
    FROM (
        SELECT data, metropolitana, min, max 
        FROM tendencia 
        ORDER BY id DESC 
        LIMIT 5
    ) AS ultimos_registros
    ORDER BY data ASC
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result