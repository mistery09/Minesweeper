"""
|Author: Syon Kadkade
|Stand: 28.01.2023
"""

class CalcField:
    """
    Class to calculate comple game field and actual index of game field (without padding)
    """

    def __init__(self, n_size):
        self.n_size = n_size
        self.field = [[0]] * ((self.n_size) **2)

        #[x+1 : ((x**2) - (x+2))]
        self.comp_index = [i for i in range(0, ((self.n_size) **2))]
        self.act_index = [i for i in range((self.n_size), ((self.n_size **2)-(self.n_size+1))) if i % (self.n_size) > 0 and (i+1) % (self.n_size)]


    

"""
if "__main__" == __name__:
    c = CalcField(8)
"""