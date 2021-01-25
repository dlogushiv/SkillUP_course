# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.)
# и поле для хранения копеек (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


class Money:
    bank = {}
    full = 0
    coin = 0
    currency = ''

    def add_money(self, add_full: int, add_coin: int):
        """ Adding money to bank account in current currency """
        bank_coin = self.bank.get(self.currency)[1]
        if add_coin + bank_coin < 100:
            self.bank.get(self.currency)[0] += add_full
            self.bank.get(self.currency)[1] += add_coin
        else:
            self.bank.get(self.currency)[0] += add_full + 1
            self.bank.get(self.currency)[1] += add_coin - 100

    def get_money(self, get_full: int, get_coin: int):
        """ Getting money from bank account in current currency """
        bank_full = self.bank.get(self.currency)[0]
        bank_coin = self.bank.get(self.currency)[1]
        if bank_coin - get_coin >= 0:
            bank_full -= get_full
            bank_coin -= get_coin
        else:
            bank_full -= get_full + 1
            bank_coin += 100 - get_coin
        if bank_full < 0:
            print('It is impossible to get money! Your current balance less then you want to get!')
        else:
            self.bank.get(self.currency)[0] = bank_full
            self.bank.get(self.currency)[1] = bank_coin

    def get_balance(self):
        """ Output balance (sum of money) to screen in current currency """
        bal_full, bal_coin, name_full, name_coin = self.bank.get(self.currency)
        if bal_full != 1:
            name_full += 's'
        if bal_coin != 1:
            name_coin += 's'
        print(f'You have {bal_full} {name_full} {bal_coin} {name_coin} on {self.currency} account.\n')


class USD(Money):
    def __init__(self, full: int, coin: int):
        self.currency = 'USD'
        self.full = full
        self.coin = coin
        if self.currency not in super().bank.keys():
            super().bank[self.currency] = [self.full, self.coin, 'dollar', 'cent']

    def add_money(self):
        add_full, add_coin = money_input_validator(self.currency, True)
        super().add_money(add_full=add_full, add_coin=add_coin)

    def get_money(self):
        get_full, get_coin = money_input_validator(self.currency, False)
        super().get_money(get_full=get_full, get_coin=get_coin)


class EUR(Money):
    def __init__(self, full: int, coin: int):
        self.currency = 'EUR'
        self.full = full
        self.coin = coin
        if self.currency not in super().bank.keys():
            super().bank[self.currency] = [self.full, self.coin, 'euro', 'cent']

    def add_money(self):
        add_full, add_coin = money_input_validator(self.currency, True)
        super().add_money(add_full=add_full, add_coin=add_coin)

    def get_money(self):
        get_full, get_coin = money_input_validator(self.currency, False)
        super().get_money(get_full=get_full, get_coin=get_coin)


class UAH(Money):
    def __init__(self, full: int, coin: int):
        """

        :param full:
        :param coin:
        """
        self.currency = 'UAH'
        self.full = full
        self.coin = coin
        if self.currency not in super().bank.keys():
            super().bank[self.currency] = [self.full, self.coin, 'gryvna', 'kop']
        else:
            super().add_money(full, coin)

    def add_money(self):
        add_full, add_coin = money_input_validator(self.currency, True)
        super().add_money(add_full=add_full, add_coin=add_coin)

    def get_money(self):
        get_full, get_coin = money_input_validator(self.currency, False)
        super().get_money(get_full=get_full, get_coin=get_coin)


def money_input_validator(currency: str, operation: bool) -> tuple:
    """
    Validator of inputted value. Check if inputted value is in float format (x.xx) with 'dot' as delimiter

    :param currency: str: type of currency (e.g. USD, EUR, UAH)
    :param operation: bool: True -> add money; False -> get money
    :return: int, int: full part of money; coin part of money
    """
    res = -1
    counter = 0
    res_f = 0
    res_c = 0
    text = 'add to' if operation else 'get from'
    while res < 0 and counter < 5:
        try:
            res = float(input(f'Input sum of money you want {text} {currency} account (delimiter: . ): '))
            res = int(round(res, 2) * 100)
            res_f = res // 100
            res_c = res % 100
        except ValueError:
            counter += 1
            if counter < 5:
                print(f'Wrong input! You have {5 - counter} attempt.')
            else:
                print('Attempts left!')
    return res_f, res_c


if __name__ == '__main__':
    usd = USD(10, 0)
    usd.add_money()
    usd.get_money()
    usd.get_balance()

    eur = EUR(20, 0)
    eur.add_money()
    eur.get_money()
    eur.get_balance()

    uah = UAH(20, 0)
    uah.add_money()
    uah.get_money()
    uah.get_balance()

    print(Money.bank)
