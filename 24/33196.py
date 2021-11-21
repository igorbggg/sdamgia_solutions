# Ссылка: https://inf-ege.sdamgia.ru/problem?id=33196

with open('33196.txt', 'r') as file:
    data = file.read()

res = {}
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    res[i] = 0

for i in range(1, len(data)):
    if data[i-1] == "A":
        res[data[i]] += 1

print(max(res, key=lambda x: res[x]))


