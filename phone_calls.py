# must be run on the internet
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf13af826fa88d4d1b52e226f1a8fe178"
# Your Auth Token from twilio.com/console
auth_token  = "aaf2a25655ce56e7bf78f532e3b27d24"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19082679550", 
    from_="+12027409056",
    body="Hello from Python!")

print(message.sid)