# https://inf-ege.sdamgia.ru/problem?id=35483

for i in range(35000000, 40000001):
    print(i)
    b = int(i ** 0.5) + 1  # находим правую границу диапазона для поиска делителей
    dividers = []  # создаем список делителей числа a
    for d in range(1, b):
        if i % d == 0:
            if d % 2 == 1:
                dividers.append(d)
            if (i // d) % 2 == 1:
                dividers.append(i // d)
        if len(dividers) > 5:
            dividers = []
            break
    if len(dividers) == 5:
        print(i)




