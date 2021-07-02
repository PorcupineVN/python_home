def thesaurus_adv(*args):
    crew = {}
    for people in args:
        name = people.split()
        if name[1][0] not in crew.keys():
            crew[name[1][0]] = {}
        if name[0][0] not in crew[name[1][0]].keys():
            crew[name[1][0]][name[0][0]] = []
        crew[name[1][0]][name[0][0]].append(people)
    return crew


dictionary = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
keys_1 = list(dictionary.keys())
keys_1.sort()
for key_1 in keys_1:
    print(key_1, ':')
    keys_2 = list(dictionary[key_1].keys())
    keys_2.sort()
    for key_2 in keys_2:
        print(f'    {key_2}: {dictionary[key_1][key_2]}')
