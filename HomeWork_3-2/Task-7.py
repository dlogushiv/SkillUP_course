# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр.
# Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром.


def is_palindrome(x):
    a = str(x)
    b = ''.join(reversed(a))
    # return True if a == b else False
    return a == b


print(is_palindrome(123326))
print(is_palindrome(123321))
