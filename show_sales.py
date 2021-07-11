import sys

comand = sys.argv
with open('bakery.csv', 'r', encoding='utf-8') as f:
    transaction_list = f.readlines()
    print(transaction_list)
    if len(comand) == 1:
        print(*transaction_list, sep='')
    elif len(comand) == 2:
        print(*transaction_list[int(comand[1])-1:], sep='')
    elif len(comand) == 3:
        print(*transaction_list[int(comand[1]) - 1 : int(comand[2])], sep='')
