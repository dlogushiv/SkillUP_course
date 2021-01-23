# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.
from random import randint


class Device:
    def __init__(self, vendor: str, model: str, year: int):
        self.vendor = vendor
        self.model = model
        self.year = year

    def work(self):
        """This method shows how the device works"""
        pass


class CoffeeMachine(Device):
    def __init__(self, vendor: str, model: str, year: int, modes: dict):
        super().__init__(vendor, model, year)
        self.modes = modes

    def work(self):
        mode = randint(1, len(self.modes))
        print(f'Coffee machine {self.vendor.capitalize()} {self.model} preparing {self.modes.get(mode)}! Wait few minutes, please!')
        print('\t\t---pf-pf-pf puf-puf-puf wzhik-wzhik-wzhik---')
        print(f'Please, take your {self.modes.get(mode)}.')

    def __str__(self) -> str:
        modes_str = ''
        for i in range(1, len(self.modes) + 1):
            modes_str += self.modes.get(i)
            if i < len(self.modes):
                modes_str += ', '
        return (f'I am coffee machine {self.vendor.capitalize()} {self.model} {self.year}-th year production. '
                f'I have next working modes: {modes_str}.')


class Blender(Device):
    def __init__(self, vendor: str, model: str, year: int, speeds: dict):
        super().__init__(vendor, model, year)
        self.speeds = speeds

    def work(self, speed: int = 1):
        print(f'Blender {self.vendor.capitalize()} {self.model} whipping a cocktail on {speed} speed.')
        print('\t\t', f'---{self.speeds.get(speed)}' * 3, '---', sep='')
        print('Your cocktail is ready!')

    def __str__(self) -> str:
        speeds_str = ''
        for i in range(1, len(self.speeds) + 1):
            speeds_str += str(i)
            if i < len(self.speeds):
                speeds_str += ', '
        return (f'I am blender {self.vendor.capitalize()} {self.model} {self.year}-th year production. '
                f'I can work on {speeds_str} speed.')


class MeatGrinder(Device):
    def __init__(self, vendor: str, model: str, year: int, reverse: bool = False):
        super().__init__(vendor, model, year)
        self.reverse = reverse

    def work(self, rev: bool = False):
        if self.reverse and rev:
            print(f'Meat grinder {self.vendor.capitalize()} {self.model} trying to return meat back!')
            print('\t\t---viu-viu-viu---')
            print('Ready!')
        else:
            if rev:
                print('I have not reverse function. So you need to disassemble me for remove the meat.')
            else:
                print(f'Meat grinder {self.vendor.capitalize()} {self.model} grinding meat!')
                print('\t\t', '---vzhuuu-zhuuu-zhuuu' * 3, '---', sep='')
                print('Ready!')

    def __str__(self) -> str:
        if self.reverse:
            return (f'I am meat grinder {self.vendor.capitalize()} {self.model} {self.year}-th year production. '
                    f'I have reverse function and can return meat back.')
        else:
            return (f'I am meat grinder {self.vendor.capitalize()} {self.model} {self.year}-th year production. '
                    f'I have not reverse function and you will manually return meat back.')


if __name__ == '__main__':
    print('\tHello!\nNow you will see how the different devices work (°_°)\n')
    coffee = CoffeeMachine('LG', '32446', 2019, {1: 'espresso', 2: 'latte', 3: 'cappuccino'})
    coffee.work()
    print(coffee)

    print()

    blender = Blender('bosch', 'GLS-43003', 2018, {1: 'uuuhh', 2: 'zh-zh', 3: 'vzhu-vzhu'})
    blender.work(speed=2)
    print(blender)

    print()

    grinder = MeatGrinder('kenwood', 'MG-3420', 2020, False)
    grinder.work(rev=True)
    print(grinder)
