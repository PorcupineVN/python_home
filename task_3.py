def thesaurus(*args):
    crew = {}
    for name in args:
        if name[0] not in crew.keys():
            crew[name[0]] = []
        crew[name[0]].append(name)
    return crew


dictionary = thesaurus("Иван", "Мария", "Петр", "Илья")
list_keys = list(dictionary.keys())
list_keys.sort()
for key in list_keys:
    print(f'"{key}" : {dictionary[key]}')
