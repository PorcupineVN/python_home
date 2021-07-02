def num_translate(numbers):
    number = input('Введите число от 1 до 10, на аглийском языке: ')
    return numbers.get(number)


numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print(num_translate(numbers))
