import logging
import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
VERSION = os.getenv('VERSION')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
client = Client(ACCOUNT_SID, AUTH_TOKEN)
url = 'https://api.vk.com/method/{}'


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'access_token': ACCESS_TOKEN,
        'v': VERSION
    }
    try:
        result = requests.post(url.format('users.get'),
                               params=params).json().get('response')
        status = result[0]['online']
    except requests.exceptions.RequestException as error:
        logging.error(f'Произошла ошибка: {error}')
        return None
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
            break
        time.sleep(5)
