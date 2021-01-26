# Создайте класс SoccerPlayer, у которого есть:
# конструктор init, принимающий 2 аргумента: name, surname.
# Также во время инициализации необходимо создать 2 атрибута экземпляра:
# goals и assists - общее количество голов и передач игрока, изначально оба значения должны быть 0
# метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# метод make_assist, который принимает количество передач, сделанных игроком за матч,
# по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>


class SoccerPlayer:
    """
    Class SoccerPlayer describe a soccer player.
    A soccer player have 4 arguments:
    name, surname -> gets from constructor;
    goals, assists -> are 0 after initialisation and increase with methods 'score' and 'make_assist'
    """

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, nog: int = 1):
        """
        Increase player's number of goals with 1 as default (or with got value 'nog')

        :param nog: number of goals
        :return:
        """
        self.goals += nog

    def make_assist(self, noa: int = 1):
        """
        Increase player's number of assists with 1 as default (or with got value 'noa')

        :param noa: number of assists
        :return:
        """
        self.assists += noa

    def statistics(self):
        """
        Print player's statistics: <Surname> <Name> - goals: <goals>, assists: <assists>
        :return:
        """
        print(f'{self.surname.capitalize()} {self.name.capitalize()} - goals: {self.goals}, assists: {self.assists}')


if __name__ == '__main__':
    player_1 = SoccerPlayer('Joe', 'Soul')
    player_2 = SoccerPlayer('Eddy', 'Harrison')
    player_1.make_assist()
    player_2.make_assist()
    player_1.make_assist()
    player_2.score()
    player_1.statistics()
    player_2.statistics()
