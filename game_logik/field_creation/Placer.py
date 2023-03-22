"""
"""
from field_creation.Marker import Marker


class Placer:
    """
    Class to place bombs and numbers in game field
    """


    def place_bombs(self, game_field, bomb_index):
        for index in bomb_index:
            game_field[index] = ["B"]

        
        return game_field



    def place_numbers(self, game_field, number_index):
        for index in number_index:
            game_field[index] = [number_index[index]]

        return game_field


"""if "__main__" == __name__:
    p = Placer()
    toy_field = [[0]] * 16
    toy_bomb_index = [7, 6]
    gf = p.place_bombs(toy_field, toy_bomb_index)

    toy_number_index = {1: 3, 2:6}

    gf = p.place_numbers(gf, toy_number_index)
    print(gf)"""

    




    