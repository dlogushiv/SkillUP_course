# Создайте программу «Фирма».
# Нужно хранить информацию о человеке: ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.


def look_base():
    if BASE:
        print('The employees base:')
        for emp in BASE:
            print('ID-' + str(emp) + ':', BASE[emp])
    else:
        print('The employees base is empty.')
    print()
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
    print('1. by employee\'s ID.')
    print('2. by employee\'s name.')
    print('3. by employee\'s phone.')
    print('4. by employee\'s email.')
    print('5. by employee\'s job position.')
    print('6. by employee\'s skype.')
    choice = correct_choice(5)
    if choice == 1:
        emp_id = search_by_id()
        del BASE[emp_id]
        print('The employee with ID %s were delete.' % emp_id)
    else:
        founded_id = search_by_param(parameters[choice - 2])
        if not founded_id:
            print('Employee not found!')
        elif len(founded_id) == 1:
            del BASE[founded_id[0][0]]
            print('The employee were delete.')
        else:
            print('Next employees found:')
            for el in founded_id:
                print(el)
            print('Check the employee\'s info. Remember the needed employee\'s ID and delete it by ID.')
    print()
    main_menu()


def search_employee():
    print('The employee searching. Please, select search method:')
    print('1. by employee\'s ID.')
    print('2. by employee\'s name.')
    print('3. by employee\'s phone.')
    print('4. by employee\'s email.')
    print('5. by employee\'s job position.')
    print('6. by employee\'s skype.')
    choice = correct_choice(6)
    if choice == 1:
        print(BASE[search_by_id()])
    else:
        founded_id = search_by_param(parameters[choice - 2])
        if not founded_id:
            print('Employee not found!')
        elif len(founded_id) == 1:
            print('Employee found:', founded_id[0])
        else:
            print('Next employees found:')
            for el in founded_id:
                print(el)
    print()
    main_menu()


def search_by_id(emp_id=0):
    if emp_id == 0:
        emp_id = correct_choice(max(BASE.keys()), 'ID')
    while BASE.get(emp_id) is None:
        print('ID not found! ', end='')
        emp_id = correct_choice(max(BASE.keys()), 'ID')
    return emp_id


def search_by_param(param=''):
    print('Search employee by %s.' % param, end=' ')
    if param == 'phone':
        val = enter_phone()
    elif param == 'email':
        val = enter_email()
    else:
        val = input('Enter %s: ' % param)
    res = []
    while not res:
        for emp_id in BASE:
            if BASE[emp_id][param].lower() == val.lower():
                res.append((emp_id, BASE[emp_id]))
        if not res:
            val = input('%s not found! Input %s again: ' % (param.capitalize(), param))
    return res


def change_employee():
    print('The employee\'s info changing. Please, select info you want to change:')
    print('1. change employee\'s name.')
    print('2. change employee\'s phone.')
    print('3. change employee\'s email.')
    print('4. change employee\'s job position.')
    print('5. change employee\'s skype.')
    choice = correct_choice(5)
    selected_param = parameters[choice - 1]
    founded_id = search_by_param(selected_param)
    if not founded_id:
        print('The employee with this %s not founded.' % selected_param)
    elif len(founded_id) > 1:
        print('More than one employee founded with this %s:' % selected_param)
        for el in founded_id:
            print(el)
        selected_id = input('Please, select the unique ID: ')
        while selected_id not in (str(el[0]) for el in founded_id):
            try_again('input', 'Input ID from list bellow.')
            selected_id = input('Input ID to change the %s' % selected_param)
        change_by_id(int(selected_id), selected_param)
    else:
        emp_id = founded_id[0][0]
        BASE[emp_id][selected_param] = input('Please, input new %s: ' % selected_param)
    print('The employee\'s info changed.\n')
    main_menu()


def change_by_id(emp_id, param):
    if param == 'phone':
        new_val = enter_phone()
    elif param == 'email':
        new_val = enter_email()
    else:
        new_val = input('Input new %s: ' % param)
    BASE[emp_id][param] = new_val


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
            phone_num = int(input('Enter the employee\'s phone (only 7...15 numbers, without +): ').replace(' ', ''))
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
        email = input('Enter the employee\'s e-mail: ').lower()
        mask = re.match(r'[\w.-]+@+[\w.-]+\.+[\w]', email)
        if not bool(mask):
            try_again('enter', 'e-mail must have format xxx@xxx.xxx')
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
        2: {'name': 'Mia Ellison', 'phone': '+8936485472', 'email': 'mia.ellison@gmail.com', 'job position': 'HR', 'skype': 'miael'},
        3: {'name': 'Mia Ellison', 'phone': '+8936485472', 'email': 'mia.ellison@gmail.com', 'job position': 'Manager', 'skype': 'miaelli'},
        4: {'name': 'Frederic Bouchon', 'phone': '+6321785214', 'email': 'fred.bouchon@true.fr', 'job position': 'Regional director',
            'skype': 'fredbouchon'}}
parameters = (list(BASE[1].keys()))

main_menu()
