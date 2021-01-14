# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, иначе False.
from datetime import date


def isDate(day: int, month: int, year: int) -> bool:
    if day in range(1, 32) and month in range(1, 13) and year > 0:
        try:
            if date(year, month, day).weekday():
                return True
        except ValueError:
            return False
    else:
        return False


# XOR-шифрование (*)
# Написать функцию XOR_cipher, принимающую 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.


def XOR_cipher(line: str, key: str) -> str:
    while len(key) != len(line):
        if len(line) < len(key):
            key = key[:len(line)]
        else:
            key += key
    cipher_line = ''
    for i in range(len(line)):
        cipher_line += chr(ord(line[i]) ^ ord(key[i]))
    return cipher_line


def XOR_uncipher(ciph_line, key):
    return XOR_cipher(ciph_line, key)


if __name__ == '__main__':
    print(isDate(13, 1, 2021))
    print(isDate(29, 2, 2021))

    a = XOR_cipher('hello', '23')
    print(a)
    print(XOR_uncipher(a, '23'))
