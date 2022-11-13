from twilio.rest import Client
import os

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
Twilio_from_number = os.environ["Twilio_from_number"]
to_number = os.environ["to_number"]


#This class is responsible for sending notifications with the deal flight details
# if a flight is found that's cheaper than what's listed in google sheet.
class NotificationManager:
    def __init__(self):
        #creating client object from client class
       self.client = Client(account_sid, auth_token)

    # send a text method via Twilio
    def text(self, message):
        message = self.client.messages.create(
            body=message,
            from_=Twilio_from_number,
            to=to_number
        )
        # notifies if text was sent successfully
        print(message.status)