# Создайте класс Point. У этого класса должны быть:
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственно в атрибуты x и y
# метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"


class Point(object):
    def set_coordinates(self, x: int, y: int):
        self.x = x
        self.y = y
        return self

    def get_distance(self, z):
        if not isinstance(z, Point):
            print('Not Point provided')
        elif self.x == z.x and self.y == z.y:
            print('The points are the same')
        else:
            return ((self.x - z.x) ** 2 + (self.y - z.y) ** 2) ** 0.5


if __name__ == '__main__':
    a = Point()
    b = Point()
    a.set_coordinates(-1, 2)
    b.set_coordinates(-1, -2)
    print(a.get_distance(b))
