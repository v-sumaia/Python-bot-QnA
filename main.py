import functions as fun
import variables

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

endpoint = variables.get('API_ENDPOINT')
credential = AzureKeyCredential(variables.get('API_KEY'))
client = ConversationAnalysisClient(endpoint, credential)

print('Bot: say something ')
while True:
    response=input('You: ')
    print(f'Bot: you said ', response)

