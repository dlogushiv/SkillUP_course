# Реализовать клас Температуры (как сегодня в конце урока),
# который на основе @property будет возвращать, присваивать данные для цельсиев, фаренгейтов и кельвинов.

class Scale:
    CEL = 'C'
    KEL = 'K'
    FAR = 'F'


class Temperature:
    TEMP_UNITS = 'CFK'

    def __init__(self, value: float, unit: str = Scale.CEL):
        self.__value = value
        if unit.capitalize() in Temperature.TEMP_UNITS:
            self.__unit = unit.capitalize()
        else:
            self.__unit = Scale.CEL
            print('Wrong units input! Units set as celsius (C).')

    def __str__(self):
        return f'Current temperature is {self.__value} °{self.__unit}.'

    def __eq__(self, other):
        return True if self.__value == other.__value and self.__unit == other.__unit else False

    @property
    def celsius(self):
        if self.__unit == Scale.CEL:
            return self.__value
        elif self.__unit == Scale.KEL:
            return round(self.__value - 273.15, 2)
        else:
            return round((self.__value - 32) * 5 / 9, 2)

    @celsius.setter
    def celsius(self, value: float):
        self.__value = value
        self.__unit = Scale.CEL

    @property
    def kelvins(self):
        if self.__unit == Scale.KEL:
            return self.__value
        elif self.__unit == Scale.CEL:
            return round(self.__value + 273.15, 2)
        else:
            return round(((self.__value - 32) * 5 / 9) + 273.15, 2)

    @kelvins.setter
    def kelvins(self, value: float):
        self.__value = value
        self.__unit = Scale.KEL

    @property
    def fahrenheits(self):
        if self.__unit == Scale.FAR:
            return self.__value
        elif self.__unit == Scale.CEL:
            return round((self.__value * 9 / 5) + 32, 2)
        else:
            return round(((self.__value - 273.15) * 9 / 5) + 32, 2)

    @fahrenheits.setter
    def fahrenheits(self, value: float):
        self.__value = value
        self.__unit = Scale.FAR


if __name__ == '__main__':
    t1 = Temperature(10)
    print(t1)
    print('In celsius it is:', t1.celsius)
    print('In kelvins it is:', t1.kelvins)
    print('In fahrenheits it is:', t1.fahrenheits)

    t1.kelvins = 25
    print(t1)
    print('In celsius it is:', t1.celsius)
    print('In kelvins it is:', t1.kelvins)
    print('In fahrenheits it is:', t1.fahrenheits)

    t1.fahrenheits = 50
    print(t1)
    print('In celsius it is:', t1.celsius)
    print('In kelvins it is:', t1.kelvins)
    print('In fahrenheits it is:', t1.fahrenheits)

    print()

    t2 = Temperature(10)
    print(t1)
    print(t2)
    print(t1 == t2)

    print()

    t2.fahrenheits = 50
    print(t1)
    print(t2)
    print(t1 == t2)
