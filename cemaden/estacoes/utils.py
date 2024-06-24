
def verificar_e_criar_tabela(connection):
  cursor = connection.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS estacoes (
      id INT AUTO_INCREMENT PRIMARY KEY,
      codestacao VARCHAR(255),
      id_tipoestacao INT,
      nome VARCHAR(255),
      INDEX(codestacao(191))
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  ''')
  connection.commit()
  cursor.close()

def process_and_store_data_estacoes(connection, resposta):
  cursor = connection.cursor()
  for estacao in resposta.json():
    cursor.execute("""
      SELECT 1 FROM estacoes WHERE codestacao = %s OR nome = %s LIMIT 1
    """, (estacao['codestacao'], estacao['nome']))
    if cursor.fetchone() is None:
      cursor.execute("""
        INSERT INTO estacoes (codestacao, id_tipoestacao, nome)
        VALUES (%s, %s, %s)
      """, (estacao['codestacao'], estacao['id_tipoestacao'], estacao['nome']))
  connection.commit()
  cursor.close()