import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_dev_key')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'hotel_db')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3307))
    # Use python dicts mapped to rows instead of tuples
    MYSQL_CURSORCLASS = 'DictCursor'
