# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC2fa452c81d34fc2952e00022a1c6e436"
auth_token = "8e6fd396cf9a650c96a5031c43997f28"

client = Client(account_sid, auth_token)

# A list of message objects with the properties described above
for message in client.messages.list():
    if message.direction == "inbound":
        print(message.body)
        thing = message.sid
        client.messages(thing).delete()

