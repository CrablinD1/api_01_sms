import time
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
url = os.getenv('URL')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'access_token': ACCESS_TOKEN,
        'v': '5.92'
    }
    result = requests.post(url, params=params).json().get('response')
    status = result[0]['online']
    return status


def sms_sender(sms_text):
    message = client.messages.create(
        to=NUMBER_TO,
        from_=NUMBER_FROM,
        body=sms_text
    )

    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            print(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
