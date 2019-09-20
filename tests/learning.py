import requests

# Example 1
# request = requests.get('http://api.open-notify.org')
# print(request.text)
# print(request.status_code)

# Example 2, ISS API
# people = requests.get('http://api.open-notify.org/astros.json')
# #print(people.text)
# people_json = people.json()
# print(people_json)

# #Printing the number of people in space
# print("Number of people in space right now: ", people_json['number'] )

# for person in people_json['people']:
# 	print('This is a person in space,', person['name'])

#Example 3, Datamuse
parameter = {"syn":"food"}
request = requests.get('https://api.datamuse.com/words',parameter)
rhyme_json = request.json()
for i in rhyme_json[0:10]:
	print(i['word'])

