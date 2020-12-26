# Напишите функцию, которая отображает на экран форматированный текст, указанный на рисунке.


def print_quote(quote, screen_length=50):
    author = quote[0]
    if quote[1][0] != '"':
        q = '"' + quote[1] + '"'
    else:
        q = quote[1]
    list_of_words = q.split(' ')
    row = list_of_words[0]+' '
    row_len = len(list_of_words[0])+1
    for i in range(1, len(list_of_words)):
        if row_len + len(list_of_words[i]) <= screen_length:
            row += list_of_words[i] + ' '
            row_len += len(list_of_words[i]) + 1
        else:
            print(row)
            row = list_of_words[i] + ' '
            row_len = len(list_of_words[i]) + 1
    print(row)
    print(f'{author:>{screen_length}}\n')


quotes = [('Oscar Wilde', 'Always forgive your enemies; nothing annoys them so much.'),
          ('Mark Twain', 'A banker is a fellow who lends you his umbrella when the sun is shining, but wants it back the minute it begins to rain.'),
          ('William James "Will" Durant', 'Education is a progressive discovery of our own ignorance.'),
          ('Mark Twain',
           'The first half of life consists of the capacity to enjoy without the chance, the last half consists of the chance without the capacity.'),
          ]

for el in quotes:
    print_quote(el, screen_length=55)
