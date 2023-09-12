import functions as fun
from variables import *
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

def main():
    try:
        endpoint = API_ENDPOINT
        credential = AzureKeyCredential(API_KEY)
        client = ConversationAnalysisClient(endpoint, credential)
        print('Bot: say something ')
        while True:
            response=input('You: ')
            print(f'Bot: you said ', response)
    except KeyboardInterrupt:
        print ('\nOk Bye')
    else:
        print ('No exceptions are caught')

if __name__ == '__main__':
    main()

