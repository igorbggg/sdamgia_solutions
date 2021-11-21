# Ссылка: https://inf-ege.sdamgia.ru/problem?id=27689

with open('27689.txt', 'r') as file:
    data = file.read()

res = []
state = 1
c = 0
for sym in data:
    if state == 1:
        if sym == 'X':
            state = 2
            c += 1
        else:
            res.append(c)
            state = 1
            c = 0
    elif state == 2:
        if sym == 'Y':
            state = 3
            c += 1
        else:
            res.append(c)
            state = 1
            c = 0
    elif state == 3:
        if sym == 'Z':
            state = 1
            c += 1
        else:
            res.append(c)
            state = 1
            c = 0
print(max(res))

