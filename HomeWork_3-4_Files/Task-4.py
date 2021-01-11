# Дан текстовый файл.
# Найти длину самой длинной строки.


def read_file(file) -> list:
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        file_list = [line for line in f.readlines()]
        f.close()
    except IOError:
        print(f'Can not read the file {file}.')
    return file_list


file_in = 'Task-4_input_file.txt'
text = read_file(file_in)
text_len = [len(line.rstrip()) for line in text]
print('Max line length:', max(text_len))
