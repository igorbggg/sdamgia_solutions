# https://inf-ege.sdamgia.ru/problem?id=33197

def find_dividers(a):
    result = []
    for divider in range(1, int(a**0.5) + 1):
        if a % divider == 0:
            result.append(divider)
            result.append(a // divider)
    return sorted(list(set(result)))


for a in range(1000000, 2000001):
    result = []
    for divider in range(1, int(a**0.5) + 1):
        if a % divider == 0:
            result.append(abs(divider - a // divider))
    c = 0
    for j in result:
        if j <= 100:
            c += 1
        if c == 3:
            print(a)
            break


