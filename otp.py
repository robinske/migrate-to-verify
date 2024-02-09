import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
verify_sid = os.environ['VERIFY_SERVICE_SID']
client = Client(account_sid, auth_token)


def send(to):
    verification = client.verify.services(verify_sid).verifications.create(to=to, channel='sms')
    return verification.status


def check(to, token):
    verification_check = client.verify.services(verify_sid).verification_checks.create(to=to, code=token)
    return verification_check.status == 'approved'