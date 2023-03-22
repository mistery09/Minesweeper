"""
|Author: Syon Kadkade
|Stand: 27.01.2023
"""

from random import choices

class SetBombs:
    """
    Class to setup game Field -> place bombs and number fields
    """

    def __init__(self, 
        n_bombs=10, 
        field_index=[11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 
        37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 65, 66, 67, 68, 
        71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88]
        ):

        self.n_bombs = n_bombs
        self.field_index = field_index
        self.n_bombs_index = None



    def get_bomb_positions(self):
        self.n_bombs_index = choices(self.field_index, k=self.n_bombs)
        return self.n_bombs_index
        

        


"""if "__main__" == __name__:
    s = SetBombs()
"""


    
