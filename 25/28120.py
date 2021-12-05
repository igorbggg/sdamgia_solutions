# https://inf-ege.sdamgia.ru/problem?id=28120

for i in range(201455, 201471):
    c = 0
    m = []
    for a in range(1, i + 1):
        if i % a == 0:
            c += 1
            m.append(a)
    if c == 4:
        print(m)
