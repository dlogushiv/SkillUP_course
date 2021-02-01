# Создайте класс Robot, у которого есть:
# атрибут класса population. В этом атрибуте будет хранится общее количество роботов, изначально принимает значение 0;
# конструктор init, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение вида "Робот <name> был создан".
# Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"


class Robot:
    population = 0

    def __init__(self, name: str):
        self.name = name
        Robot.population += 1

    def destroy(self):
        if Robot.population > 0:
            print(f'A robot {self.name} was destroyed.')
            Robot.population -= 1
            del self
        else:
            print('No one robot left.')

    def say_hello(self):
        print(f'A robot {self.name} greets you, human species')

    @staticmethod
    def how_many():
        print(f'The robots population is {Robot.population} robots.')


if __name__ == '__main__':
    r1 = Robot('r1-rc')
    r2 = Robot('r2-rdst')
    r2.how_many()
    r1.say_hello()
    r1.destroy()
    r2.destroy()
    r1.destroy()
