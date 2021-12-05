# https://inf-ege.sdamgia.ru/problem?id=2335

for i in range(1, 26):
    p = i
    c = ''
    while p > 0:
        c = str(p % 2) + c
        p = p // 2
    if c[-3:] == '101':
        print(i)





