# Ссылка: https://inf-ege.sdamgia.ru/problem?id=27694

with open('27694.txt', 'r') as file:
    data = file.read()

res = []
state = 1
c = 0
for sym in data:
    if state == 1:
        if sym == 'A':
            state = 2
            c += 1
        else:
            res.append(c)
            state = 1
            c = 0
    elif state == 2:
        if sym == 'B':
            state = 1
            c += 1
        else:
            res.append(c)
            state = 1
            c = 0
print(max(res))

