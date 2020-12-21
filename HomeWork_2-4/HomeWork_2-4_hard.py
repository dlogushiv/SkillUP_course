# Создайте программу «Фирма».
# Нужно хранить информацию о человеке: ФИО, телефон, рабочий email, название должности, номер кабинета, skype.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.


# import csv
#
#
# def csv_reader():
#     with open('BaseOfEmployees.csv', 'r') as base:
#         # with open('TB_data_dictionary_2020-12-21.csv', 'r') as base:
#         reader = csv.reader(base)
#         for row in reader:
#             print(', '.join(row))
#     base.close()
#
#
# def csv_dict_reader():
#     with open('BaseOfEmployees.csv', 'r') as base_dict:
#         reader = csv.DictReader(base_dict)
#         for line in reader:
#             print(line['Name'], line['Phone'], line['email'], line['job position'], line['skype'])
#     base_dict.close()


def look_base():
    print('The employees base:')


def add_employee():
    print('Add')


def del_employee():
    print('Delete')


def search_employee():
    print('Search')


def change_employee():
    print('Change')


def try_again():
    print('Wrong selection! Try again.')


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
                try_again()
        except ValueError:
            print('Please, make correct choice! Press button 1 - 5 and enter')
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
base['employee 1'] = {'name': 'Joe Martin', 'phone': '+7654896547', 'email': 'joe.martin@gmail.com', 'job position': 'chief', 'skype': 'jmartin'}
base['employee 2'] = {'name': 'Mia Elison', 'phone': '+8936485472', 'email': 'mia.elison@gmail.com', 'job position': 'HR', 'skype': 'miael'}
base['employee 3'] = {'name': 'Frederic Bouchon', 'phone': '+6321785214', 'email': 'fred.bouchon@true.fr', 'job position': 'regional director',
                      'skype': 'fredbouchon'}
main_menu()
