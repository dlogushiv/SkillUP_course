# Создайте класс Person, у которого есть:
# конструктор init, принимающий 3 аргумента: first_name, last_name, age.
# метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;


class Person:
    """
    Class Person describe a simple person.
    A person have 3 arguments:
    first_name, last_name, age -> gets from constructor
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        """
        Print person's full name: <Last name> <First name>
        :return:
        """
        print(f'{self.last_name.capitalize()} {self.first_name.capitalize()}')

    def is_adult(self) -> bool:
        return True if self.age >= 18 else False


if __name__ == '__main__':
    v = Person('vanya', 'dl', 34)
    c = Person('cloud', 'bouche', -9)
    x = Person('xavier', 'deboche', 18)
    v.full_name()
    print(v.is_adult())
    c.full_name()
    print(c.is_adult())
    x.full_name()
    print(x.is_adult())
