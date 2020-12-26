# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


def fill_square(size, symbol='*', is_filled=True):
    symbol += ' '
    if is_filled:
        for i in range(size):
            print(symbol * size)
    else:
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(symbol, end='')
                else:
                    print('  ', end='')
            print()
    print()


fill_square(10, '0', True)
fill_square(10, '0', False)
