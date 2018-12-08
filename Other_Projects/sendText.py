from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5896caeea01e2ed9ac84734d7cd3c92a"
# Your Auth Token from twilio.com/console
auth_token  = "316e3281e8a4ae29932140ef6f3fe88f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16265038376", 
    from_="+12528889215",
    body="Fujimak Pan!")

print(message.sid)