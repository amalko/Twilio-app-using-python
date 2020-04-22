

from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

my_msg = "Hello Amal, it's me Twilio"

message = client.messages.create(to= my_cell, from_= my_twilio, body= my_msg)