import requests
from load_env import user_cemaden, password_cemaden, cemaden_api_token
import schedule
import time
from utils import process_and_store_data
from db_utils import create_table, create_connection

def cemaden():
  
  connection = create_connection()
  create_table(connection)
  
  token_url = cemaden_api_token
  login = {'email': user_cemaden, 'password': password_cemaden}
  response = requests.post(token_url, json=login)

  if response.status_code == 200:
    content = response.json()
    token = content['token']

    sws_url = 'http://sws.cemaden.gov.br/PED/rest/pcds-acum/acumulados-recentes'
    params = dict(codibge=2607901)
    r = requests.get(sws_url, params=params, headers={'token': token})

    if r.status_code == 200:
      process_and_store_data(r)
    else:
      print("Erro ao obter dados: ", r.status_code)
  else:
    print("Erro ao obter token: ", response.status_code)

def job():
  print("I'm working...")
  cemaden()
  print("Dados inseridos com sucesso!")

# Agendar a tarefa para ser executada a cada 3 minutos
schedule.every(3).minutes.do(job)

try: 
  cemaden()
  while True:
    schedule.run_pending()
    time.sleep(60)
except Exception as e:
    print('Erro ao executar o script:', e)