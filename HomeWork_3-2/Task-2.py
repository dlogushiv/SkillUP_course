# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.

def even_nums(a, b):
    if a > b:
        a, b = b, a
    for num in range(a + 1, b):
        if num % 2 == 0:
            print(num, end='; ')
    print()


even_nums(6, 17)
even_nums(17, 6)
