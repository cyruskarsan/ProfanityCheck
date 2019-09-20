from twilio.rest import Client
import requests

account_sid = 'ACe23a5bc04f6382c9c984cbd2fd4154d5'
auth_token = '4b4aaf5dc63221ef1b3934948dec7a44'

client  = Client(account_sid,auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = 'Hi, Fun Fact, Number of people in space right now is' + str(number_iss)

# formulate the message that will be sent
message = client.messages.create(
	to ="4086033036",
	from_="19495777952",
	body = Message
	)

print(message.status)