import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = response.content.decode(encoding=response.encoding)
users = {}
with open('nginx_logs.txt', 'w+', encoding='utf-8') as f:
    f.write(content)
    f.seek(0)
    for line in f:
        st = line.split()
        if st[0] not in users.keys():
            users[st[0]] = 1
        else:
            users[st[0]] += 1
spamer_name = ''
spamer_result = 0
for key, value in users.items():
    if value > spamer_result:
        spamer_result = value
        spamer_name = key
print(spamer_name, spamer_result)
