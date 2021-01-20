# Реализуйте класс «Автомобиль».
# Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Car:
    def __init__(self, vendor: str, model: str, year: int, engine: int, color: str, price: float):
        self.vendor = vendor
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price

    @staticmethod
    def create():
        vendor = input('Input the vendor name: ')
        model = input('Input the model name: ')
        year = int(input('Input the production year: '))
        engine = int(input('Input the engine volume (cm3): '))
        color = input('Input the car colour: ')
        price = float(input('Input the car price: '))
        return Car(vendor, model, year, engine, color, price)

    def __str__(self):
        return f'The car is {self.color} {self.vendor.capitalize()} {self.model.capitalize()} {self.year}-th production ' \
               f'with engine {self.engine} cm3. It price is {self.price}.'

    def get_vendor(self): return self.vendor

    def get_model(self): return self.model

    def get_year(self): return self.year

    def get_engine(self): return self.engine

    def get_colour(self): return self.color

    def get_price(self): return self.price


if __name__ == '__main__':
    # first_car = Car.create()
    first_car = Car('audi', 'a6', 2020, 3000, 'red', 40000)
    print(first_car)
    print(first_car.color)
    print(first_car.model)
