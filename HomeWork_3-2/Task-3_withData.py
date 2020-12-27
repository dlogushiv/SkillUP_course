def fill_square(size, symbol='*', is_filled=True):
    res = [[symbol]*size for i in range(size)]
    if not is_filled:
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                res[i][j] = ' '
    return res


for el in fill_square(5, '#', True):
    print(*el)
print()
for el in fill_square(5, '#', False):
    print(*el)
