def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i


n = int(input('До какого числа продолжать генерировать нечётные числа?  '))
nums = odd_nums(n)
for _ in range(1, n + 3, 2):
    try:
        print(next(nums))
    except StopIteration:
        print("...StopIteration...")
