import functions as fun
from variables import *

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

endpoint = API_ENDPOINT
credential = AzureKeyCredential(API_KEY)
client = ConversationAnalysisClient(endpoint, credential)

print(endpoint)
print('Bot: say something ')
while True:
    response=input('You: ')
    print(f'Bot: you said ', response)

