# Дан текстовый файл. Найти и заменить в нем заданное слово.
# Что искать и на что заменять определяется пользователем.
import string


def read_file(file) -> list:
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        file_list = [line for line in f.readlines()]
        f.close()
    except IOError:
        print(f'Can not open the file {file}.')
    return file_list


def write_file(file, lines: list):
    try:
        f = open(file, 'w', encoding='utf8')
        f.writelines(lines)
        f.close()
    except IOError:
        print(f'Can not write to the file.')


def search_and_replace(s_word: str, r_word: str, file):
    """
    Function read a file, search the s_word in it, replace s_word to r_word and write a file with r_word

    :param s_word: word for search -> str
    :param r_word: word for replace -> str
    :param file: file name
    """
    text = read_file(file)
    for j in range(len(text)):
        words = text[j].split(' ')
        for i in range(len(words)):
            # if word is last in line and it is not empty line
            if words[i][-1:] == '\n' and len(words[i]) > 2:
                if words[i][-2] in string.punctuation:
                    sym = words[i][-2]
                    if words[i][:-2] == s_word:
                        words[i] = r_word + sym + '\n'
            # if word's last symbol is punctuation
            elif words[i][-1] in string.punctuation:
                sym = words[i][-1]
                if words[i][:-1] == s_word:
                    words[i] = r_word + sym
            # if last 2 symbols is 's (e.g. John's; cat's; land's)
            elif words[i][-2:] == '\'s':
                if words[i][:-2] == s_word:
                    words[i] = r_word + '\'s'
            elif words[i] == s_word:
                words[i] = r_word
        text[j] = ' '.join(words)
    write_file(file, text)


my_file = 'Task-6_File.txt'
search_and_replace('forest', 'land', my_file)
search_and_replace('John', 'Bob', my_file)
search_and_replace('land', 'forest', my_file)
search_and_replace('Bob', 'John', my_file)
