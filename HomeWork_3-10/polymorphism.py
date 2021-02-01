# Написать маленькую программу, которая на Ваше усмотрение, реализует полиморфизм. Пример придумать самим


class Animal:
    def i_am(self):
        print('I am animal!', end=' ')

    def speak(self):
        print('I can speak.', end=' ')

    def feature(self):
        print('I am different.')


class Cat(Animal):

    def i_am(self):
        print('I am cat!', end=' ')

    def speak(self):
        print('I say mur-mau.', end=' ')

    def feature(self):
        print('I can see in the dark.')


class Dog(Animal):

    def i_am(self):
        print('I am dog!', end=' ')

    def speak(self):
        print('I say gaf-gaf.', end=' ')

    def feature(self):
        print('I can guard.')


class Mouse(Animal):

    def i_am(self):
        print('I am mouse!', end=' ')

    def speak(self):
        print('I say pi-pi.', end=' ')

    def feature(self):
        print('I can crawl into tight spaces.')


class Horse(Animal):

    def i_am(self):
        print('I am horse!', end=' ')

    def speak(self):
        print('I say i-go-go.', end=' ')

    def feature(self):
        print('I can run very quickly.')


class Bird(Animal):

    def i_am(self):
        print('I am bird!', end=' ')

    def speak(self):
        print('I say chirik-chirik.', end=' ')

    def feature(self):
        print('I can fly.')


if __name__ == '__main__':
    class Person():
        def __init__(self, name: str):
            self.name = name


    def animal_characteristics(x):
        for animal in x:
            if isinstance(animal, Animal):
                animal.i_am()
                animal.speak()
                animal.feature()
            else:
                print('Current element is not animal!')


    p = Person('Vanya')
    c = Cat()
    d = Dog()
    m = Mouse()
    h = Horse()
    b = Bird()
    sp = [c, d, b, m, h, p, c, b, m]
    animal_characteristics(sp)
