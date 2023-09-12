import os 
from dotenv import dotenv_values, load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_ENDPOINT = os.getenv('API_ENDPOINT')