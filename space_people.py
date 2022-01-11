import requests

people = requests.get('http://api.open.notif.org/astros.json')
json = people.json()

print(json)
print('The people currently in space are:')
for p in json['people']:
    print(p['name'])