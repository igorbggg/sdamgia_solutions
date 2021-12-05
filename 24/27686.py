# Ссылка: https://inf-ege.sdamgia.ru/problem?id=27686

with open('27686.txt', 'r') as file:
    data = file.read()

c = 1
res = []
for i in range(1, len(data)):
    if data[i] == 'X' and data[i-1] == 'X':
        c += 1
    else:
        res.append(c)
        c = 1

print(max(res))