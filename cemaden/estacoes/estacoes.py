import requests
import sys
sys.path.append('cemaden')
from load_env import cemaden_api_token, password_cemaden, user_cemaden
from db_utils import create_connection
from utils import process_and_store_data_estacoes, verificar_e_criar_tabela

def estacoes():
  
  connection = create_connection()
  verificar_e_criar_tabela(connection)
  
  token_url = cemaden_api_token
  login = {'email': user_cemaden, 'password': password_cemaden}
  response = requests.post(token_url, json=login)

  if response.status_code == 200:
    content = response.json()
    token = content['token']

    sws_url = 'http://sws.cemaden.gov.br/PED/rest//pcds-cadastro/estacoes?'
    params = dict(codibge=2607901)
    r = requests.get(sws_url, params=params, headers={'token': token})

    if r.status_code == 200:
      process_and_store_data_estacoes(connection, r)
    else:
      print("Erro ao obter dados: ", r.status_code)
  else:
    print("Erro ao obter token: ", response.status_code)
    
try:
  estacoes()
except Exception as e:
  print("Erro ao executar o script: ", e)
