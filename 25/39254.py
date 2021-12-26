# https://inf-ege.sdamgia.ru/problem?id=39254

def find_dividers(a):
    result = []
    for divider in range(1, int(a**0.5) + 1):
        if a % divider == 0:
            result.append(divider)
        if len(result) == 6:
            break
    return sorted(list(set(result)))


for i in range(500000001, 600000000):
    dividers = find_dividers(i)
    if len(dividers[1:6]) == 5:
        res = dividers[1] * dividers[2] * dividers[3] * dividers[4] * dividers[5]
        if res < i:
            print(res)
