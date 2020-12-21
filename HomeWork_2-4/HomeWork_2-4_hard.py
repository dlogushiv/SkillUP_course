# Создайте программу «Фирма».
# Нужно хранить информацию о человеке: ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.


def look_base():
    print('The employees base:')
    for emp in base:
        print('id' + str(emp) + ':', base[emp])
    main_menu()


def add_employee():
    print('New employee adding.')
    next_id = max(base.keys()) + 1
    name = input('Enter the name of new employee: ').title()
    phone = enter_phone()
    email = enter_email()
    position = input('Enter the job position of new employee: ').capitalize()
    skype = input('Enter the skype of new employee: ').lower()
    base[next_id] = {'name': name, 'phone': phone, 'email': email, 'job position': position, 'skype': skype}
    print('New employee added!\n')
    main_menu()


def del_employee():
    print('Delete')


def search_employee():
    print('Search')


def change_employee():
    print('Change')


def try_again(s1, s2):
    print('Wrong %s! Please, make correct enter! %s' % (s1, s2))


def enter_phone():
    phone = ''
    while len(phone) not in range(7, 16):
        try:
            phone_num = int(input('Enter the phone (only 7...15 numbers, without +) of new employee: ').replace(' ', ''))
            phone = str(phone_num)
            if len(phone) not in range(7, 16):
                try_again('enter', 'Only 7...15 numbers')
        except ValueError:
            try_again('enter', 'Only 7...15 numbers')
    return '+' + phone


def enter_email():
    import re
    email = ''
    mask = False
    while not bool(mask):
        email = input('Enter the e-mail of new employee: ').lower()
        mask = re.match(r'[\w.-]+@+[\w.-]+\.+[\w]', email)
        if not bool(mask):
            try_again('enter', 'e-mail must have symbol @')
    return email


def main_menu():
    print('Select an action. Press the correspond button and enter.')
    print('1. Look the base.')
    print('2. Add a new employee.')
    print('3. Delete the employee.')
    print('4. Search the employee.')
    print('5. Change the employee\'s info.')
    print('6. Exit.')
    choice = 0
    while choice not in range(1, 7):
        try:
            choice = int(input('Make your choice: '))
            if choice not in range(1, 7):
                try_again('selection', 'Press button 1 - 5 and enter')
        except ValueError:
            try_again('enter', 'Press button 1 - 5 and enter')
    if choice == 1:
        look_base()
    elif choice == 2:
        add_employee()
    elif choice == 3:
        del_employee()
    elif choice == 4:
        search_employee()
    elif choice == 5:
        change_employee()
    else:  # choice == 6
        print('Goodbye!')


base = {}
base[1] = {'name': 'Joe Martin', 'phone': '+7654896547', 'email': 'joe.martin@gmail.com', 'job position': 'Chief', 'skype': 'jmartin'}
base[2] = {'name': 'Mia Elison', 'phone': '+8936485472', 'email': 'mia.elison@gmail.com', 'job position': 'HR', 'skype': 'miael'}
base[3] = {'name': 'Frederic Bouchon', 'phone': '+6321785214', 'email': 'fred.bouchon@true.fr', 'job position': 'Regional director',
           'skype': 'fredbouchon'}
main_menu()
