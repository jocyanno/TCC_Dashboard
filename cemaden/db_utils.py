import mysql.connector
from load_env import db_database, db_host, db_password, db_port, db_user

def create_connection():
  
  connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    port=db_port
  )

  return connection

def connection_close(connection):
  connection.close()

def create_table(connection):
  cursor = connection.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados_cemaden (
      id INT AUTO_INCREMENT PRIMARY KEY,
      acc120hr FLOAT,
      acc12hr FLOAT,
      acc1hr FLOAT,
      acc24hr FLOAT,
      acc3hr FLOAT,
      acc48hr FLOAT,
      acc6hr FLOAT,
      acc72hr FLOAT,
      acc96hr FLOAT,
      codestacao VARCHAR(255),
      codibge INT,
      datahora DATETIME,
      id_estacao INT
    )
  """)
  connection.commit()
  cursor.close()

def insert_data(connection, data):
  cursor = connection.cursor()
  
  query_check = """
  SELECT EXISTS(
    SELECT 1 FROM dados_cemaden WHERE codestacao = %s AND datahora = %s
  )
  """
  cursor.execute(query_check, (data[9], data[11]))
  exists = cursor.fetchone()[0]
  
  if not exists:
    query_insert = """
    INSERT INTO dados_cemaden (
      acc120hr, acc12hr, acc1hr, acc24hr, acc3hr, acc48hr, acc6hr, acc72hr, acc96hr,
      codestacao, codibge, datahora, id_estacao
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query_insert, data)
    connection.commit()
  cursor.close()