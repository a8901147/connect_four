from disk import Disk
from game import Game
from player import Player


mock_name = ["Jeremmy", "Wayne"]
mock_color = [Disk.RED, Disk.YEL]
target_score = 2
rows_size = 6
cols_size = 7

game = Game(mock_name, mock_color, target_score, rows_size, cols_size)
game.game_start()
"""

a = {
    1:"a",
    2:"b"
}
print(list(a.keys()))
print(type(list(a.keys())))
"""