# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
from random import randint


def list_sum(data):
    summa = 0
    for el in data:
        summa += el
    return summa


# Задание 2
# Напишите функцию для нахождения минимума в списке целых.
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def list_min(data):
    m = data[0]
    for i in range(1, len(data)):
        if data[i] < m:
            m = data[i]
    return m


# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых.
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def simple_quant(data):
    res = 0
    for el in data:
        n = el
        counter = 0
        for i in range(2, n):
            if el % i == 0:
                counter += 1
        if el != 1 and counter == 0:
            res += 1
    return res


# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число.
# Из функции нужно вернуть количество удаленных элементов.
def removed_quant(data: list, n):
    quant = 0
    for el in data:
        if el == n:
            quant += 1
            data.pop(el)
    return quant


# Задание 5
# Напишите функцию, которая получает два списка в качестве параметра и возвращает список, содержащий элементы обоих списков.
def both_lists(data1, data2):
    return data1 + data2


# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента списка целых.
# Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
# Функция возвращает новый список, содержащий полученные результаты.
def list_degree(data, n):
    res = []
    for el in data:
        res.append(el ** n)
    return res


input_list_1 = list(randint(1, 10) for i in range(10))
input_list_2 = list(randint(1, 10) for i in range(10))
print(*input_list_1)
print(*input_list_2)
print('summa =', list_sum(input_list_1))
print('min =', list_min(input_list_1))
print('quantity of simple =', simple_quant(input_list_1))
print('quantity of removed 2 =', removed_quant(input_list_1, 2))
print('elements of both lists =', *both_lists(input_list_1, input_list_2))
print('list degree =', *list_degree(input_list_1, 2))
