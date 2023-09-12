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
        while response != 'exit':
            response = input('You: ')
            output = client.get_answers(
                question=response,
                project_name="QnA-bot",
                deployment_name="test"
            )
            for candidate in output.answers:
                print("Bot: {}".format(candidate.answer))
    except KeyboardInterrupt:
        print('\nOk Bye')
    except TypeError:
        print('Enter a valid response.')


if __name__ == '__main__':
    main()