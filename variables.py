import os 
from dotenv import dotenv_values, load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_ENDPOINT = os.getenv('API_ENDPOINT')
SEARCH_SERVICE_API_KEY=os.getenv('SEARCH_SERVICE_API_KEY')
SEARCH_SERVICE_QUERY_KEY=os.getenv('SEARCH_SERVICE_QUERY_KEY')
BOT_PREDECTION_URL=os.getenv('BOT_PREDECTION_URL')
OCP_APIM_SUBSCRIPTION_KEY=os.getenv('Ocp-Apim-Subscription-Key')