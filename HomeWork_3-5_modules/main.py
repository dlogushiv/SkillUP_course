from services import isDate, XOR_cipher, XOR_uncipher

print('\t1. Is your date real?')
flag = True
counter = 0
while flag and counter < 5:
    try:
        d, m, y = (int(el) for el in input('Input the date.month.year: ').split('.'))
        flag = False
        print('\tYour date is real!\n' if isDate(d, m, y) else '\tYour date is not real!\n')
    except:
        counter += 1
        if counter < 5:
            print(f'Incorrect input. {5 - counter} attempts left. Try again.')
        else:
            print('\tGoodbye!\n')

print('\t2. XOR encrypting')
line = input('Input the text for encrypting: \n')
key = input('Input the key for encrypting: \n')
encrypted_line = XOR_cipher(line, key)
print('Your encrypted text:')
print(encrypted_line)
print('Your unencrypted text: \n')
print(XOR_uncipher(encrypted_line, key))
