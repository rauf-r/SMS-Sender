from twilio.rest import Client

account_sid = 'your id here'
auth_token = 'your auth_token here'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+1.........',
    body='JARVIS here! Good Morning!',
    to='+1..........'
    )

print(message.sid)
