import json

peoples = {}
with open('users.csv', 'r') as users, open('hobby.csv', 'r') as hobby:
    for user in zip(users, hobby):
        key = user[0].split(',')
        key[2] = key[2].rstrip()
        key = ' '.join(key)
        value = user[1].split(',')
        value[-1] = value[-1].rstrip()
        value = ' '.join(value)
        if value == '':
            value = None
        peoples[key] = value

with open('result.txt', 'w') as f:
    json.dump(peoples, f)
with open('result.txt') as json_file:
    data = json.load(json_file)
    for key, value in data.items():
        print(key, value)
