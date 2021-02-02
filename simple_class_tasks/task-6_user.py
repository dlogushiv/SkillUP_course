# Написать класс User, в котором защищенным доступом к паролю.
# Пароль должен быть строкой от 5 до 12 знаков включительно и содержать хотя бы одну цифру.
# Создать текстовый файл easy_password и проверить не находится ли пароль в этом файле.
# Примеры легких паролей для файла easy_password:
# 123456
# qwerty
# password
# 123456789
#
# в ините 2 значения: логин и пароль
#
# з.ы. проверка пароля на наличие в файле - отдельным статикметодом


class User:

    def __init__(self, name: str):
        self.name = name
        self.__pass = None

    @property
    def password(self):
        return self.__pass

    @password.setter
    def password(self, password: str):
        if User.is_password_correct(password) and User.is_password_easy(password):
            self.__pass = password

    def __str__(self):
        if self.password:
            return f'User name: {self.name}. User password: {self.password}.'
        else:
            return f'User name: {self.name}. User password: not set.'

    @staticmethod
    def is_password_easy(password: str):
        pass_file = 'task-6_easy_passwords.txt'
        f = open(pass_file, 'r', encoding='utf8')
        for line in f.readlines():
            if password == line.rstrip():
                return False
        f.close()
        return True

    @staticmethod
    def is_password_correct(password: str):
        if 5 <= len(password) <= 12:
            for symbol in password:
                if symbol.isdigit():
                    return True
        return False


if __name__ == '__main__':
    # a = User.is_password_easy('123456')
    # b = User.is_password_correct('qwqwqwqwqwq1')
    # print(a)
    # print(b)

    u1 = User('user1')
    u1.password = 'QWERTY1'
    u2 = User('user2')
    u2.password = '1234567890123'
    print(u1)
    print(u2)
