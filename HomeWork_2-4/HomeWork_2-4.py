# Задание: Есть три кортежа целых чисел, необходимо:
# 1. найти элементы, которые есть во всех кортежах.
# 2. найти элементы, которые уникальны для каждого кортежа.
# 3. найти элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.

def check(x, y, z):
    res = []
    length = min((len(x), len(y), len(z)))
    for i in range(length):
        if x[i] == y[i] and x[i] == z[i]:
            res.append(x[i])
    return tuple(res)


a = (5, 6, 2, 1, 11, 9, 7, 3, 21, 2)
b = (2, 6, 7, 2, 9, 3, 4, 4, 9, 2)
c = (5, 6, 7, 2, 9, 9, 3, 9, 4, 2)
res1 = set(a + b + c)
res2a = (el for el in a if a.count(el) <= 1)
res2b = (el for el in b if b.count(el) <= 1)
res2c = (el for el in c if c.count(el) <= 1)
res3 = check(a, b, c)

print(*res1)
print(*res2a)
print(*res2b)
print(*res2c)
print(*res3)
