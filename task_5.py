import random


def get_jokes(n, *args):
    result = []
    for i in range(n):
        joke = ''
        for element in args:
            joke += random.choice(element) + ' '
        joke = joke.rstrip(' ')
        result.append(joke)
    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input('Введите необходимое количество шуток: '))
print(get_jokes(n, nouns, adverbs, adjectives))