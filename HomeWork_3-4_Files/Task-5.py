# Дан текстовый файл.
# Посчитать сколько раз в нем встречается заданное пользователем слово.
import string


def read_file(file) -> str:
    file_list = []
    try:
        f = open(file, 'r', encoding='utf8')
        for line in f.readlines():
            for word in line.lower().strip().split(' '):
                if word[-1:] in string.punctuation:
                    file_list.append(word[:-1])
                else:
                    file_list.append(word)
        f.close()
    except IOError:
        print(f'Can not read the file {file}.')
    return ' '.join(file_list)


def search_word(word: str, in_text: str) -> int:
    return in_text.split(' ').count(word)


file_in = 'Task-5_Input_file.txt'
search = input('Input the word for search: ')
text = read_file(file_in)
print(f'Count of word "{search}" in the file:', search_word(search, text))
