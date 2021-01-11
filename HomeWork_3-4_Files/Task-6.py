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


def search_and_replace(s_word: str, r_word: str, text: list) -> list:
    """
    Function search the s_word in the text and replace it to r_word

    :param s_word: word for search -> str
    :param r_word: word for replace -> str
    :param text: list with str elements as lines from the file
    :return: the list with srt elements and replaced words
    """
   