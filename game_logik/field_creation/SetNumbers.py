"""
"""
from field_creation.Marker import Marker

class SetNumbers:

    def get_number_positions(self, n_size, game_field, act_index):
        """
        """
        numbers = {}

        for index in act_index:
            if game_field[index][0] == "B":
                continue

            count_bomb = 0
            positions = self.__get_positions(index, n_size)

                

            for position in positions:
                
                if game_field[position][0] == "B":
                    count_bomb += 1

            numbers[index] = count_bomb

        return numbers


    def __get_positions(self, index, n_size):
        """
        Helper function for "get_number_positions"
        Calculate for the current positions it's neighbors 3x3

        Variable explination:
        index = current looked position (always center)

        l = left side of index
        r = right side of inde
        t = top of index
        d = down of index

        tl = topf left of index
        tr = top right of index

        dl = down left of index
        dr = down right of index

        [tl] [t] [tr]
        [l] [index] [r]
        [dl] [d] [dr]
        """

        l = index -1
        r = index + 1
        t = index - n_size
        d = index + n_size

        tl = t -1
        tr = t + 1
        
        dl = d - 1
        dr = d + 1

        return [l, r, t, d, tl, tr, dl, dr]



"""if "__main__" == __name__:
    sn = SetNumbers()
    toy_size = 4
    #4x4
    toy_field = [[0], [0], [0], [0], 
                 [0], [Marker.BOMB], [0], [0], 
                 [0], [Marker.BOMB], [Marker.BOMB], [0], 
                 [0], [0], [0], [0]] 

    toy_index = [5, 6, 9, 10]

    toy_numbers = sn.get_number_positions(toy_size, toy_field, toy_index)"""
    
