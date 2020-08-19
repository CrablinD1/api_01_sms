import time
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv('access_token')
twilio_account_sid = os.getenv('twilio_account_sid')
twilio_auth_token = os.getenv('twilio_auth_token')
URL = os.getenv('url')
NUMBER_FROM = os.getenv('phone_from')
NUMBER_TO = os.getenv('phone_to')


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'access_token': access_token,
        'v': '5.92'
    }
    result = requests.post(URL, params=params).json().get('response')
    status = result[0]['online']
    return status


def sms_sender(sms_text):
    client = Client(twilio_account_sid, twilio_auth_token)

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
