# Напишите функцию, которая считает количество цифр в числе.
# Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.

def numb_of_digits(a):
    if type(a) != str:
        a = str(a)
    return len(a)


x = input('Input the number: ')
print('Your number length =', numb_of_digits(x))
x = 3456
print('Length of 3456=', numb_of_digits(x))
