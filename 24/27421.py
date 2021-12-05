# Ссылка: https://inf-ege.sdamgia.ru/problem?id=27421

# 1 способ чтения файлов
file = open('27421.txt', 'r')
data = file.read()
file.close()

# 2 способ чтения файлов
with open('27421.txt', 'r') as file:
    data = file.read()

res = []

c = 1
for i in range(1, len(data)):
    if data[i] != data[i-1]:
        c += 1
    else:
        res.append(c)
        c = 1

print(max(res))
