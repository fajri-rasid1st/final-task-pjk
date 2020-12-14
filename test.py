rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

cols = zip(*rows)

print(list(list(cols)[0]))