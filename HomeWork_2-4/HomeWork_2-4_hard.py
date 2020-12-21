# Создайте программу «Фирма».
# Нужно хранить информацию о человеке: ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.


def look_base():
    print('The employees base:')
    for emp in BASE:
        print('id' + str(emp) + ':', BASE[emp])
    main_menu()


def add_employee():
    print('New employee adding.')
    next_id = max(BASE.keys()) + 1
    name = input('Enter the name of new employee: ').title()
    phone = enter_phone()
    email = enter_email()
    position = input('Enter the job position of new employee: ').capitalize()
    skype = input('Enter the skype of new employee: ').lower()
    BASE[next_id] = {'name': name, 'phone': phone, 'email': email, 'job position': position, 'skype': skype}
    print('New employee added!\n')
    main_menu()


def del_employee():
    print('Employee deleting. Please, select deleting method:')
    print('1. via employee\'s ID.')
    print('2. via employee\'s name.')
    print('3. via employee\'s phone.')
    print('4. via employee\'s email.')
    print('5. via employee\'s skype.')
    choice = correct_choice(5)
    if choice == 1:
        print('Deleting employee via ID.')
        emp_id = correct_choice(max(BASE.keys()), 'ID')
        while BASE.get(emp_id) == None:
            print('ID not found! ', end='')
            emp_id = correct_choice(max(BASE.keys()), 'ID')
        del BASE[emp_id]
        print('The employee with ID %s were delete.' % emp_id)
    # todo
    elif choice == 2:
        print('Deleting employee via name.')
    elif choice == 3:
        print('3. via employee\'s phone.')
    elif choice == 4:
        print('4. via employee\'s email.')
    else:  # choice == 5
        print('5. via employee\'s skype.')
    main_menu()


def search_employee():
    print('Search')


def change_employee():
    print('Change')


def correct_choice(n, s1=''):
    choice = 0
    while choice not in range(1, n + 1):
        try:
            if s1 and 'of' not in s1:
                s1 = ' of ' + s1
            choice = int(input('Make your choice%s: ' % s1))
            if choice not in range(1, n + 1):
                try_again('selection', 'Input number from 1 to %s and press enter' % n)
        except ValueError:
            try_again('enter', 'Input number from 1 to %s and press enter' % n)
    return choice


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
    choice = correct_choice(6)
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


BASE = {1: {'name': 'Joe Martin', 'phone': '+7654896547', 'email': 'joe.martin@gmail.com', 'job position': 'Chief', 'skype': 'jmartin'},
        2: {'name': 'Mia Ellison', 'phone': '+8936485472', 'email': 'mia.elison@gmail.com', 'job position': 'HR', 'skype': 'miael'},
        4: {'name': 'Frederic Bouchon', 'phone': '+6321785214', 'email': 'fred.bouchon@true.fr', 'job position': 'Regional director',
            'skype': 'fredbouchon'}}
# print(max(BASE.keys()))
# print(BASE.get(3))
# main_menu()
del_employee()
