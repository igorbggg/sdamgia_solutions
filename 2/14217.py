from itertools import product


def func(z, y, x, w):
    return z and not y and (w <= x)


combinations = list(product([True, False], repeat=4))

print('?', '?', '?', '?', 'F')
for c in combinations:
    print(int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(func(*c)))
