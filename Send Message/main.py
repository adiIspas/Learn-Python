from twilio.rest import TwilioRestClient

account_sid = "AC8d38bfc2e8f5b7adf08c4d971b4879ad" # Your Account SID from www.twilio.com/console
auth_token = "{{ 9683f1488f79ae7c70a2482795e3d1a3 }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+4076158xxxx",    # Replace with your phone number
    from_="+40316301728") # Replace with your Twilio number

print(message.sid)
