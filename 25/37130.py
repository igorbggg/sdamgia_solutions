# https://inf-ege.sdamgia.ru/problem?id=37130


def find_dividers(a):
    ''' Функция возвращает все натуральные делители числа a '''
    return [i for i in range(2, a) if a % i == 0]


c = 0
for i in range(600000, 1000000):
    dividers = find_dividers(i)
    min_div = -1
    for j in dividers:
        if j % 10 == 7 and j != 7 and j != i:
            min_div = j
            c += 1
            print(i, min_div)
            break
    if c == 5:
        break
