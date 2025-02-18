if __name__ == "__main__":
    # Write your solution here
    class Rapers:
        """
        Базовый класс реперы
        """
        def __init__(self, name: str, money: float, alive: bool, albums: list):
            """
            Инициализация репера
            :param name: имя репера
            :param money: количество у него денег
            :param alive: статус его состояния здоровья
            :param albums: выпущенные им альбомы
            """
            self.alive = alive
            self.name = name
            self.money = money
            self.albums = albums

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, new_name: str) -> None:
            if not isinstance(new_name, str):
                raise TypeError("name должно быть переменной типа str")
            self._name = new_name

        @property
        def money(self) -> float:
            return self._money

        @money.setter
        def money(self, new_money: float) -> None:
            if not isinstance(new_money, float):
                raise TypeError("money должно быть переменной типа float")
            self._money = new_money

        @property
        def alive(self) -> bool:
            return self._alive

        @alive.setter
        def alive(self, new_alive: bool) -> None:
            if not isinstance(new_alive, bool):
                raise TypeError("alive должно быть переменной типа bool")
            self._alive = new_alive

        @property
        def albums(self) -> list:
            return self._albums

        @albums.setter
        def albums(self, new_albums: list) -> None:
            if not isinstance(new_albums, list):
                raise TypeError("albums должно быть типом list")
            self._albums = new_albums

        def __str__(self):
            return f"Имя исполнителя: {self._name}, Количество выпущенных альбомов: {len(self.albums)}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, money={self.money!r}, alive={self.alive!r}, albums={self.albums!r})"


        def release_album(self, name_album, required_money, profit_money) -> None:
            """
            Метод позволяет выпустить альбом
            :param name_album: название нового альбома
            :param required_money: количество денег необходимое для выпуска альбома
            :param profit_money: количество денег, которое получит репер после выпуска альбома
            :return:
            """
            if not self.alive:
                raise TypeError("К сожалению, состояние здоровья репера не позволяет выпустить ему альбом")
            if self.money < required_money:
                raise TypeError("К сожалению, у репера не хватает денег на выпуск альбома")
            self.albums.append(name_album)
            self.money = self.money - required_money + profit_money

        def rest_in_peace(self):
            """
            Метод позволяет изменить статус состояния здоровья репера на False
            :return:
            """
            if not self.alive:
                raise TypeError("К сожалению, состояние здоровья репера не позволят ему еще раз умереть")
            self.alive = False


    class RussianRapers(Rapers):
        """
        Дочерний класс базового класса Реперы: Русские реперы
        """
        def __init__(self, name: str, money: float, alive: bool, inoagent_status: bool, albums: list):
            """
            Инициализация русского репера. Русские реперы наследуют все атрибуты базового класса Реперы, однако у них есть дополнительный атрибус в виде статуса иноагента
            :param name: имя репера
            :param money: количество у него денег
            :param alive: статус его состояния здоровья
            :param inoagent_status: статус иноагента
            :param albums: выпущенные им альбомы
            """
            super().__init__(name, money, alive, albums)
            self._inoagent_status = inoagent_status

        @property
        def inoagent_status(self) -> bool:
            return self._inoagent_status

        @inoagent_status.setter
        def inoagent_status(self, new_inoagent_status: bool) -> None:
            if not isinstance(new_inoagent_status, bool):
                raise TypeError("inoagent_status должно быть переменной типа bool")
            self._inoagent_status = new_inoagent_status

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, money={self.money!r}, alive={self.alive!r}, albums={self.albums!r}, inoagent_status={self.inoagent_status!r})"


        def release_album(self, name_album, required_money, profit_money) -> None:
            """
            Перегрузка метода release_album связана с тем, что на территории РФ действуют особые законы, которые затрудняют выпуск альбома реперам, имеющим статус иноагента.
            :param name_album: Название нового альбома
            :param required_money: количество денег необходимое для выпуска альбома
            :param profit_money: количество денег, которое получит репер после выпуска альбома
            :return:
            """
            if not self.alive:
                raise TypeError("К сожалению, состояние здоровья репера не позволяет выпустить ему альбом")
            if self._inoagent_status:
                raise TypeError("К сожалению, статус иноагента репера не позволяет выпустить ему альбом")
            if self.money < required_money:
                raise TypeError("К сожалению, у репера не хватает денег на выпуск альбома")
            self.albums.append(name_album)
            self.money = self.money - required_money + profit_money


    EgorKreed = RussianRapers('Егор Крид', 1000000.0, True, False, ['Холостяк', '58', 'Pussyboy', '<3'])
    print(repr(EgorKreed))
    print(str(EgorKreed))
    EgorKreed.release_album('Новый альбом Егор Крида',321123, 112321123)
    print(repr(EgorKreed))
    pass
