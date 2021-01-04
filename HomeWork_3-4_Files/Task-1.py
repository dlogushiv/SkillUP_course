# Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку из каждого файла.

def read_file(file) -> list:
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        for line in f.readlines():
            file_list.append(line)
        f.close()
    except FileNotFoundError:
        print('File not found!')
    return file_list


def excess_lines(list_1, list_2):
    len_1 = len(list_1)
    len_2 = len(list_2)
    if len(list_1) < len(list_2):
        diff = len_2 - len_1
        for _ in range(diff):
            list_1.append('\n')
    elif len(list_1) > len(list_2):
        diff = len_1 - len_2
        for _ in range(diff):
            list_2.append('\n')
    return list_1, list_2


file_1 = 'Task-1_File-1.txt'
file_2 = 'Task-1_File-2.txt'
file_list_1 = read_file(file_1)
file_list_2 = read_file(file_2)
if file_list_1 and file_list_2:
    file_list_1, file_list_2 = excess_lines(file_list_1, file_list_2)
    result = []
    zip_files = list(zip(file_list_1, file_list_2))
    for i in range(len(zip_files)):
        if zip_files[i][0] != zip_files[i][1]:
            result.append((i, zip_files[i][0], zip_files[i][1]))
    if result:
        for i in range(len(result)):
            print('\tDifference in line:', result[i][0] + 1)
            print('Line from file 1:', result[i][1].rstrip())
            print('Line from file 2:', result[i][2].rstrip())
    else:
        print('The not empty lines in the files are equals.')
else:
    print('One of the files is empty or not found. Please, check the files.')
