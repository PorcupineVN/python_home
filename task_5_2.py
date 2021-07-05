n = int(input('До какого числа продолжать генерировать нечётные числа?  '))
nums = (num for num in range(1, n + 1, 2))
for _ in range(1, n + 3, 2):
    try:
        print(next(nums))
    except StopIteration:
        print("...StopIteration...")