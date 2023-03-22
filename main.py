"""
A main file to run hole application.

|Author: Syon Kadkade
|Stand: 02.02.2023
"""

from game_logik import CreateField
from gui import Gui



if "__main__" == __name__:
    field_size = 10
    n_bombs = 20


    while None != True:

        c = CreateField()
        game_field, actual_index, bomb_index = c.create_field(field_size, n_bombs)

        g = Gui(field_size+2, game_field=game_field, actual_index=actual_index, n_bombs=len(bomb_index))

        if g.status:
            break
