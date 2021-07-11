import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = response.content.decode(encoding=response.encoding)
result = []
with open('nginx_logs.txt', 'w+', encoding='utf-8') as f:
    f.write(content)
    for line in f:
        st = line.split()
        element = (st[0], st[5][1:], st[6])
        result.append(element)

with open('porcupine_logs.txt', 'w+', encoding='utf-8') as p:
    for el in result:
        s = str(el)
        p.write(s)
