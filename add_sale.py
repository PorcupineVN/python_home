import sys

transaction = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{transaction}\n')
