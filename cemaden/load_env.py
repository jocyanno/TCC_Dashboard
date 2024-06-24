import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_database = os.getenv("DB_DATABASE")

cemaden_api_token = os.getenv("URL_CEMADEN_GET_TOKEN")

user_cemaden = os.getenv("CEMADEN_USER")
password_cemaden = os.getenv("CEMADEN_USER_PASS")