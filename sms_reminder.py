from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

#Load Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")

def send_sms(to_phone, patient_name, appointment_time):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = f'Reminder: Hi {patient_name}, your appointment is scheduled for {appointment_time}.',
        from_= twilio_phone,
        to=to_phone
    )
