import os
import random

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def store_token(phone_number, token, date_sent):
    """
    Required:
    - Store token with the user's phone number in your database
    - Set token expiration
    """
    pass


def send(to):
    from_ = os.environ['TWILIO_SENDER_ID']

    # generate a 6 digit token
    token = random.randint(100000, 999999)
    message = f"Your verification code is: {token}"

    msg = client.messages.create(body=message, from_=from_, to=to)
    store_token(to, token, msg.date_sent)
    return msg.sid


def fetch_token(phone_number):
    """
    Required:
    - Fetch the token stored with the user's phone number from database
    - Ensure the token is not expired
    """
    pass


def check(to, token):
    valid = fetch_token(to) == token

    if valid:
        # delete the token from the database
        pass

    return valid