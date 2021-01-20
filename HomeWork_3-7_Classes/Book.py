# Реализуйте класс «Книга».
# Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Book:
    def __init__(self, title: str, year: int, publisher: str, genre: str, author: str, price: float):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year: int):
        if new_year in range(1000, 2021):
            self.__year = new_year
        else:
            print('Wrong year input!')

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher):
        self.__publisher = new_publisher

    @property
    def genre(self):
        return self.__genre

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print('The price cannot be less 0.')

    def __str__(self) -> str:
        return f'The book of {self.author.title()} \"{self.title.capitalize()}\" in genre {self.genre} was published by {self.publisher} ' \
               f'in {self.year} have cost {self.price}'

    @staticmethod
    def add_book():
        title = input('Input the title of the book: ')
        author = input('Input the book author\'s name: ')
        genre = input('Input the genre of the book: ')
        publisher = input('Input the publisher: ')
        year = int(input('Input the year of publication: '))
        price = float(input('Input the price of the book: '))
        return Book(title, year, publisher, genre, author, price)


if __name__ == '__main__':
    new_book = Book('Some title', 2020, 'Some publisher', 'Detective', 'John Carry', 15.99)
    print(new_book)
    print(new_book.publisher)
    new_book.price = 45.89
    print(new_book.price)
    second_book = Book.add_book()
    print(second_book)
    second_book.year = 2220
    print(second_book.year)
    second_book.price = -1
    print(second_book)
