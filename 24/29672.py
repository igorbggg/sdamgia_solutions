# Ссылка: https://inf-ege.sdamgia.ru/problem?id=29672

with open('29672.txt', 'r') as file:
    data_list = [row for row in file if row.count('E') > row.count('A')]

print(len(data_list))