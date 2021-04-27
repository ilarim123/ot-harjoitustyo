import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

USERS_FILENAME = os.getenv('USERS_FILENAME') or 'users.csv'
USERS_FILE_PATH = os.path.join(dirname, '..', 'data', USERS_FILENAME)


