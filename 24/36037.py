# https://inf-ege.sdamgia.ru/problem?id=36037

with open('36037.txt', 'r') as file:
    data = file.read()


c = 0
max_c = 0
for i in range(len(data)-3):
    if data[i:i+4] == 'XZZY':
        max_c = max(c + 3, max_c)
        c = 0
    else:
        c += 1

print(max_c)