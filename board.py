from disk import Disk


class Board:
    def __init__(self, rows_size: int, cols_size: int):
        self.__rows_size = rows_size
        self.__cols_size = cols_size
        self.grid = self.init_board(rows_size, cols_size)

    @staticmethod
    def init_board(rows_size: int, cols_size: int):
        return [[Disk.EMP for i in range(cols_size)] for j in range(rows_size)]

    def display_grid(self):
        for row in range(len(self.grid)-1,-1,-1):
            print(self.grid[row])

    @property
    def rows_size(self):
        return self.__rows_size

    @property
    def cols_size(self):
        return self.__cols_size
