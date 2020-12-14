# Два списка целых заполняются случайными числами.
# Необходимо:
# 1 Сформировать третий список, содержащий элементы обоих списков;
# 2 Сформировать третий список, содержащий элементы обоих списков без повторений;
# 3 Сформировать третий список, содержащий элементы общие для двух списков;
# 4 Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# 5 Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
from random import randint

list1 = [randint(-10, 10) for i in range(10)]
list2 = [randint(-10, 10) for i in range(15)]
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 2, 4, 4, 6]

task1 = list1 + list2
task2 = [el for el in list1 if el not in list2] + [el for el in list2 if el not in list1]
task2_1 = [el for el in list1 + list2 if el not in list1 or el not in list2]
task3 = [el for el in list1 if el in list2] + [el for el in list2 if el in list1]
task4 = [el for el in list1 if list1.count(el) == 1] + [el for el in list2 if list2.count(el) == 1]
task5 = [min(list1), max(list1), min(list2), max(list2)]

print('List 1: ', list1)
print('List 2: ', list2)
print()

print('Task 1: Union of lists:\n', task1)
print('Task 2: Union of lists, without repetitions:\n', task2)
print('Task 2-1: Union of lists, without repetitions:\n', task2_1)
print('Task 3: Union of lists, common elements:\n', task3)
print('Task 4: Union of lists, unique elements:\n', task4)
print('Task 5: Min and Max elements from both lists:\n', task5)
