import mysql.connector
from load_env import db_host, db_password, db_port, db_user, db_database_deslizamentos

def create_connection_tendencia_Ocorrencias():
  
  connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database_deslizamentos,
    port=db_port
  )

  return connection
