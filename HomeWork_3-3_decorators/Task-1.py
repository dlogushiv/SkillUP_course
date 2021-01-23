# Написать функцию-декоратор, которая возводит в квадрат значение, которое возвращает функция, к которой декоратор применяется.


def decor(f):
    def wrapper(a):
        res = f(a) ** 2
        return res

    return wrapper


def func1(n):
    return n


@decor
def func2(x):
    return x


print(func1(4))
print(func2(4))
