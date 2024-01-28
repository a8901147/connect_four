import enum


class Player:
    def __init__(self, name: str, color: enum):
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color
