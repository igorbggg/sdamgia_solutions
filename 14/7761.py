# Ссылка: https://inf-ege.sdamgia.ru/problem?id=7761

res = bin(4**2020 + 2**2017 - 15)  # функция bin преобразует в двоичную систему счисления
res_str = str(res)  # функция str преобразует в строковый тип

ones = 0  # счетчик единиц
for sym in res_str:  # перебираем строку res_str
    if sym == '1':
        ones += 1

print(ones)