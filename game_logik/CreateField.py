"""
"""
import sys
sys.path.append("./game_logik/")

from field_creation import *

class CreateField:
    


    def create_field(self, n_size, n_bombs):
        """
        Method to create game field and place bombs and numbers.

        :param n_size: Size of gamefield.
        :type n_size: int
        
        :param n_bombs: Number of bombs to place
        :type n_bombs: int

        :return: gamefield
        :rtype: list[int]
        """
        self.n_size = n_size+2

        #create Game field, itself, actual index (without padding) and with padding (complete index) and 
        c = CalcField(n_size=self.n_size)
        game_field = c.field
        
        actual_index = c.act_index
        
        #complete_index = c.comp_index

        #get bomb positions
        sb = SetBombs(n_bombs=n_bombs, field_index=actual_index)
        bomb_index = sb.get_bomb_positions()
        
        #place bombs
        p = Placer()
        game_field = p.place_bombs(game_field=game_field, bomb_index=bomb_index)
        

        #get counts for field around bombs
        sn = SetNumbers()
        number_index =  sn.get_number_positions(n_size=self.n_size, game_field=game_field, act_index=actual_index)

        game_field = p.place_numbers(game_field=game_field, number_index=number_index)
        

        return game_field, actual_index, bomb_index



"""if "__main__" == __name__:
    c = CreateField()
    game_field, _ = c.create_field(4, 2)
    print(game_field)"""



