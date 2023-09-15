import functions as fun
from variables import *
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:   
        endpoint = API_ENDPOINT
        credential = AzureKeyCredential(API_KEY)
        client = QuestionAnsweringClient(endpoint, credential)

        response = ''
        print('Bot: say something.')
        while True:
            response = input('You: ')
            if response != 'exit' and response != 'Exit':
                output = fun.get_response_from_bot(response)
                for candidate in output:
                    print("Bot: {}".format(candidate["answer"]))
            else:
                print("Bot: Ok Bye")
                exit(0)

    except KeyboardInterrupt:
        print('\nOk Bye')
    except TypeError:
        print('Enter a valid response.')


if __name__ == '__main__':
    main()