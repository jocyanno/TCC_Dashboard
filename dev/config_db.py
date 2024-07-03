# import mysql.connector
import pymysql.cursors
from load_env import db_database_cemaden, db_host, db_password, db_port, db_user

def create_connection():
  
  connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database_cemaden,
    port=int(db_port)
  )

  return connection

def consultar_estacoes_disponiveis():
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM estacoes")
  result = cursor.fetchall()
  cursor.close()
  connection.close()
  return result

def consultar_ultimo_registro_estacao(codigo_estacao):
  connection = create_connection()
  cursor = connection.cursor()
  query = """
  SELECT d.*, e.nome 
  FROM dados_cemaden d
  JOIN estacoes e ON d.codestacao = e.codestacao
  WHERE d.codestacao = %s 
  ORDER BY d.datahora DESC 
  LIMIT 1
  """
  cursor.execute(query, (codigo_estacao,))
  result = cursor.fetchone()
  cursor.close()
  connection.close()
  return result

def consultar_estacoes_disponiveis_e_ultimos_registros():
  connection = create_connection()
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM estacoes")
  estacoes = cursor.fetchall()
  cursor.close()
  connection.close()
  
  ultimos_registros = []
  for estacao in estacoes:
    codigo_estacao = estacao[1]
    ultimo_registro = consultar_ultimo_registro_estacao(codigo_estacao)
    if ultimo_registro:
      ultimos_registros.append(ultimo_registro + (estacao[2],))
    else:
      ultimos_registros.append(None)
  return ultimos_registros
