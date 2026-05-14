import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_dev_key')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'hotel_db')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_CURSORCLASS = 'DictCursor'
    # Required for some cloud providers like Aiven
    MYSQL_CUSTOM_OPTIONS = {"ssl": {"ca": "/etc/ssl/certs/ca-certificates.crt"}} if os.environ.get('RENDER') else {}
