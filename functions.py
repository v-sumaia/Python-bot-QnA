import requests
import json
from variables import *

def get_response_from_bot(question):

    url = BOT_PREDECTION_URL
    payload = "{ 'question': \"" + question + "\"" "}"
    headers = { 'Ocp-Apim-Subscription-Key': OCP_APIM_SUBSCRIPTION_KEY , 'Content-Type': 'application/json' }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["answers"]
