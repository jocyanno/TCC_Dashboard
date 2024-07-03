import os
from dotenv import load_dotenv


load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

db_database_cemaden = os.getenv("DB_DATABASE_CEMADEN")
db_database_apac = os.getenv("DB_DATABASE_APAC")
db_database_cemaden_historico = os.getenv("DB_DATABASE_CEMADEN_HISTORICO")

cemaden_api_token = os.getenv("URL_CEMADEN_GET_TOKEN")
user_cemaden = os.getenv("CEMADEN_USER")
password_cemaden = os.getenv("CEMADEN_USER_PASS")