# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате),
# класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.


class Ship:
    ship_type = ''
    model = ''
    weapons = None
    year = 0

    def work(self):
        """This method shows how the ship works"""
        pass


class Frigate(Ship):
    def __init__(self, model: str, year: int, cannons: int):  # cannon - пушка, арт. орудие
        self.ship_type = 'Frigate'
        self.model = model
        self.weapons = True
        self.year = year
        self.cannons = cannons

    def work(self):
        print(f'The {self.ship_type} {self.model} goes to sink an enemy ship with cannons.')

    def __str__(self) -> str:
        return f'I am {self.ship_type} {self.model} {self.year}-th year production. I have {self.cannons} cannons on board.'


class Destroyer(Ship):
    def __init__(self, model: str, year: int, torpedoes: int):
        self.ship_type = 'Destroyer'
        self.model = model
        self.year = year
        self.weapons = True
        self.torpedoes = torpedoes

    def work(self):
        print(f'The {self.ship_type} {self.model} goes to sink an enemy ship with torpedoes.')

    def __str__(self) -> str:
        return f'I am {self.ship_type} {self.model} {self.year}-th year production. I have {self.torpedoes} torpedoes on board.'


class Cruiser(Ship):
    def __init__(self, model: str, year: int, mines: int, rockets: int):
        self.ship_type = 'Cruiser'
        self.model = model
        self.year = year
        self.weapons = True
        self.mines = mines
        self.rockets = rockets

    def work(self, mine: bool = True, rocket: bool = True):
        if not mine and not rocket:
            print(f'The {self.ship_type} {self.model} has no weapon to fight!')
        else:
            print(f'The {self.ship_type} {self.model} goes to sink an enemy ship with', end=' ')
            if mine and rocket:
                print('mines and rockets.')
            else:
                if mine:
                    print('mines.')
                if rocket:
                    print('rockets.')

    def __str__(self) -> str:
        return f'I am {self.ship_type} {self.model} {self.year}-th year production. I have {self.mines} mines and {self.rockets} rockets on board.'


if __name__ == '__main__':
    print('\t\tHello!\nLet\'s talk about ships (°_°)\n')
    frigate = Frigate('FT-20', 2010, 20)
    frigate.work()
    print(frigate)

    print()

    dest = Destroyer('DST-40', 2015, 40)
    dest.work()
    print(dest)

    print()

    cruiser = Cruiser('CCK-12', 2009, 120, 12)
    cruiser.work()
    cruiser.work(mine=False)
    cruiser.work(rocket=False)
    cruiser.work(mine=False, rocket=False)
    print(cruiser)
