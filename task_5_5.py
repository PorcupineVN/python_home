src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# вариант через множества
unique_numb = set()
repeat_numb = set()
for numb in src:
    if numb in repeat_numb:
        continue
    elif numb in unique_numb:
        repeat_numb.add(numb)
        unique_numb.discard(numb)
    else:
        unique_numb.add(numb)
list_unique = []
for numb in src:
    if numb in unique_numb:
        list_unique.append(numb)
print(list_unique)

# вариант через словари
numbers = {}
list_unique_2 = []
for numb in src:
    if numb not in numbers.keys():
        numbers[numb] = 1
    else:
        numbers[numb] += 1
for key, value in numbers.items():
    if value == 1:
        list_unique_2.append(key)
print(list_unique_2)
