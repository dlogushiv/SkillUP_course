from Money import *


def first_menu():
    print('\tWhat do you want to do?:')
    print('1. Create currency account')
    print('2. Exit')
    choice = correct_choice(2)
    if choice == 1:
        create_account()
    else:  # choice == 0
        print('Goodbye!')


def main_menu():
    print('\tWhat do you want to do?:')
    print('1. Create currency account')
    print('2. Add money to account')
    print('3. Get money from account')
    print('4. See balance on account')
    print('5. See balances on all accounts')
    print('6. Exit')
    choice = correct_choice(6)
    if choice == 1:
        create_account()
    elif choice == 2:
        add_to_account()
    elif choice == 3:
        get_from_account()
    elif choice == 4:
        account_balance()
    elif choice == 5:
        print('\tIn your bank present next accounts:') if len(my_bank.bank) > 1 else print('\tIn your bank present next account:')
        for key, value in my_bank.bank.items():
            print(f'{key} : {value[0]}.{value[1]}')
        print()
        main_menu()
    else:  # choice == 6
        print('Goodbye!')


def create_account():
    global uah, usd, eur
    print('\tSelect an available currency:')
    print('1. UAH - Ukrainian hryvna')
    print('2. USD - dollar of USA')
    print('3. EUR - European euro')
    print('4. Back to main menu')
    print('5. Exit')
    choice = correct_choice(5)
    if choice == 1:
        if 'UAH' not in my_bank.bank.keys():
            uah = UAH(0, 0)
            if uah.currency in my_bank.bank.keys():
                print(f'\t{uah.currency} account created successfully!')
            else:
                print(f'\tSomething goes wrong. {uah.currency} account was not created.')
        else:
            print('\tUAH already present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 2:
        if 'USD' not in my_bank.bank.keys():
            usd = USD(0, 0)
            if usd.currency in my_bank.bank.keys():
                print(f'\t{usd.currency} account created successfully!')
            else:
                print(f'\tSomething goes wrong. {usd.currency} account was not created.')
        else:
            print('\tUSD already present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 3:
        if 'EUR' not in my_bank.bank.keys():
            eur = EUR(0, 0)
            if eur.currency in my_bank.bank.keys():
                print(f'\t{eur.currency} account created successfully!')
            else:
                print(f'\tSomething goes wrong. {eur.currency} account was not created.')
        else:
            print('\tEUR already present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 4:
        main_menu()
    else:  # choice == 5
        print('Goodbye!\n')
    print()
    main_menu()


def add_to_account():
    global uah, usd, eur
    print('\tSelect a currency:')
    print('1. UAH - Ukrainian hryvna')
    print('2. USD - dollar of USA')
    print('3. EUR - European euro')
    print('4. Back to main menu')
    print('5. Exit')
    choice = correct_choice(5)
    if choice == 1:
        if 'UAH' in my_bank.bank.keys():
            uah.add_money()
        else:
            print('\tUAH not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 2:
        if 'USD' in my_bank.bank.keys():
            usd.add_money()
        else:
            print('\tUSD not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 3:
        if 'EUR' in my_bank.bank.keys():
            eur.add_money()
        else:
            print('\tEUR not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 4:
        main_menu()
    else:  # choice == 5
        print('Goodbye!\n')
    main_menu()


def get_from_account():
    global uah, usd, eur
    print('\tSelect a currency:')
    print('1. UAH - Ukrainian hryvna')
    print('2. USD - dollar of USA')
    print('3. EUR - European euro')
    print('4. Back to main menu')
    print('5. Exit')
    choice = correct_choice(5)
    if choice == 1:
        if 'UAH' in my_bank.bank.keys():
            uah.get_money()
        else:
            print('\tUAH not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 2:
        if 'USD' in my_bank.bank.keys():
            usd.get_money()
        else:
            print('\tUSD not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 3:
        if 'EUR' in my_bank.bank.keys():
            eur.get_money()
        else:
            print('\tEUR not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 4:
        main_menu()
    else:  # choice == 5
        print('Goodbye!\n')
    main_menu()


def account_balance():
    global uah, usd, eur
    print('\tSelect a currency:')
    print('1. UAH - Ukrainian hryvna')
    print('2. USD - dollar of USA')
    print('3. EUR - European euro')
    print('4. Back to main menu')
    print('5. Exit')
    choice = correct_choice(5)
    if choice == 1:
        if 'UAH' in my_bank.bank.keys():
            uah.get_balance()
        else:
            print('\tUAH not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 2:
        if 'USD' in my_bank.bank.keys():
            usd.get_balance()
        else:
            print('\tUSD not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 3:
        if 'EUR' in my_bank.bank.keys():
            eur.get_balance()
        else:
            print('\tEUR not present in your bank! Return to main menu!\n')
            main_menu()
    elif choice == 4:
        main_menu()
    else:  # choice == 5
        print('Goodbye!\n')
    main_menu()


def correct_choice(n):
    choice = 0
    while choice not in range(1, n + 1):
        try:
            choice = int(input('\tMake your choice: '))
            if choice not in range(1, n + 1):
                try_again('selection', 'Input number from 1 to %s and press enter' % n)
        except ValueError:
            try_again('enter', 'Input number from 1 to %s and press enter' % n)
    print()
    return choice


def try_again(s1, s2):
    print('Wrong %s! Please, make correct enter! %s' % (s1, s2))


print('\tWelcome to your bank!')
print('but remember:')
print('\t\t\t"Money often costs too much". Emerson')
print()

my_bank = Money()
uah = 0
usd = 0
eur = 0
first_menu()
# print(Money.__subclasses__())
