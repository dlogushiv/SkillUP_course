# Дан текстовый файл.
# Удалить из него последнюю строку.
# Результат записать в другой файл.


def read_file(file) -> list:
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        file_list = [line for line in f]
        f.close()
    except IOError:
        print(f'Can not read the file {file}.')
    return file_list


def write_file(lines: list):
    try:
        f = open('Task-3_Output_file.txt', 'w', encoding='utf8')
        f.writelines(lines)
        f.close()
    except IOError:
        print(f'Can not write to the file.')


file_in = 'Task-3_Input_file.txt'
text = read_file(file_in)
write_file(text[:-1])
