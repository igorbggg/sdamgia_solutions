with open('37347.txt', 'r') as file:
    data = [int(i) for i in file.readlines() if i != '\n']


print(data)
c = 0
res = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] * data[j] % 14 != 0:
            c += 1
            res.append(data[i] + data[j])
print(c, max(res))
