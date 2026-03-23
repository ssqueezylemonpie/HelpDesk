import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', ''),
        database=os.environ.get('DB_NAME', 'helpdesk_db')
    )
    return connection
