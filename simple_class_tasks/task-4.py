# Создайте класс Dog, у которого есть:
# конструктор init, принимающий 2 аргумента: name, age.
# метод description, который возвращает строку в виде "<name> is <age> years old"
# метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name.capitalize()} is {self.age} years old'

    def speak(self, sound: str):
        return f'{self.name.capitalize()} says {sound}'


if __name__ == '__main__':
    # Для проверки
    jack = Dog("Jack", 4)
    print(jack.description())  # распечатает 'Jack is 4 years old'
    print(jack.speak("Woof Woof"))  # распечатает 'Jack says Woof Woof'
    print(jack.speak("Bow Wow"))  # распечатает 'Jack says Bow Wow'
