# Дан текстовый файл.
# Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# 1 количество символов
# 2 количество строк
# 3 количество гласных букв
# 4 количество согласных букв
# 5 количество цифр


def read_file(file):
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        for line in f.readlines():
            file_list.append(line)
        f.close()
    except IOError:
        print('Can not read the file %s' % file)
    return file_list


def write_file(symbols=0, lines=0, vowel=0, consonant=0, numbers=0):
    try:
        f = open('Task-2_Output_file.txt', 'w', encoding='utf8')
        f.write('Symbols: %s\n' % symbols)
        f.write('Lines: %s\n' % lines)
        f.write('Vowel letters: %s\n' % vowel)
        f.write('Consonant letters: %s\n' % consonant)
        f.write('Numbers: %s\n' % numbers)
        f.close()
    except IOError:
        print('Can not write to the file')


def file_statistics(lines: list):
    symb = 0
    lin = 0
    vow = 0
    cons = 0
    numb = 0
    lin = len(lines)
    for line in lines:
        current_line = line.rstrip().lower()
        symb += len(current_line)
        for el in current_line:
            if el in VOWEL:
                vow += 1
            if el in CONSONANT:
                cons += 1
            if el in NUMBERS:
                numb += 1
    return symb, lin, vow, cons, numb


VOWEL = 'аеёиоуыэюя' + 'aeiouy'
CONSONANT = 'бвгджзйклмнпрстфхцчшщьъ' + 'bcdfghjklmnpqrstvwxyz'
NUMBERS = '0123456789'
file_in = 'Task-2_Input_file.txt'
text = read_file(file_in)
# stat = file_statistics(text)
# print(*stat)
write_file(*file_statistics(text))
