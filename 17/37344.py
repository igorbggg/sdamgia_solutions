# https://inf-ege.sdamgia.ru/problem?id=37344

with open('37344.txt', 'r') as file:
    data = [int(i) for i in file.readlines()]

# 1 способ (неэффективный)
res = []
for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
        if (data[i] * data[j]) % 10 == 0:
            res.append(data[i]+data[j])
print(len(res), max(res))


# 2 способ
k2 = []
k5 = []
k10 = []
for i in data:
    if i % 10 == 0:
        k10.append(i)
    elif i % 5 == 0:
        k5.append(i)
    elif i % 2 == 0:
        k2.append(i)

k = len(k2)*len(k5) + len(k10)*(len(data) - len(k10))
for i in range(len(k10) - 1):
    for j in range(i+1, len(k10)):
        k += 1
print(k)