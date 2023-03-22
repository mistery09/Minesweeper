"""
A gui file which contains the gui class.

|Author: Syon Kadkade
|Stand: 02.02.2023
"""
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox



class Gui:
    """
    A class to display and interact the minesweper game field.
    """

    def __init__(self, n_size, game_field, actual_index, n_bombs):

        self.n_size = n_size - 2
        self.game_field = game_field
        self.actual_index = actual_index
        self.flag_counter = n_bombs
        self.status = False
        self.repr = {}
        self.buttons = []
        self.index = []
        self.bomb_index = [] #save bombs itself
        self.bomb_index2 = [] #save index of bombs   
        self.flag_index = [] 

        row = 0
        number_button = 0

        


        #create dictionary to save fields in rows
        for key in range(0, self.n_size):
            self.repr[key] = []

        
        
        for i, index in enumerate(self.actual_index):


            if i == 0:
                self.repr[row] +=  [game_field[index][0]]

            elif i % self.n_size == 0:
                
                row += 1
                self.repr[row] +=  [game_field[index][0]]
                
                
            else:
                self.repr[row] +=  [game_field[index][0]]




        #create windows
        self.root = Tk()
        self.root.geometry("1000x700")
        self.root.title("Minesweeper")

        self.frame3 = Frame(self.root)
        self.frame3.place(x=475, y=70)

        self.frame2 = Frame(self.root)
        self.frame2.place(x=675, y=75)

        self.frame1 = Frame(self.root)
        self.frame1.place(x=250, y=100)



        
        self.flag_shower = Label(self.frame2, text=f'Number of Flags: {self.flag_counter}')
        self.flag_shower.pack()

        self.exit = Button(self.frame3, text="EXIT", command=self.exit)
        self.exit.pack()



        #load textures and resize it
        self.empty = self.resized("gui/textures/unrevealed.png")
        self.revealed = self.resized("gui/textures/revealed.png")
        self.flag = self.resized("gui/textures/flag.png")

        self.one = self.resized("gui/textures/one.png")
        self.two = self.resized("gui/textures/two.png")
        self.three = self.resized("gui/textures/three.png")
        self.four = self.resized("gui/textures/four.png")
        self.five = self.resized("gui/textures/five.png")
        self.six = self.resized("gui/textures/six.png")
        self.seven = self.resized("gui/textures/seven.png")
        self.eight = self.resized("gui/textures/eight.png")

        self.bomb = self.resized("gui/textures/bomb.png")


        #generate and display game field with labels
        for key in self.repr:
            for colum_index, item in enumerate(self.repr[key]):

                #Save Buttons which are not bombs
                if item == "B":
                    self.buttons.append(Label(self.frame1, text="-", image=self.empty))
                    self.buttons[number_button].bind("<Button>", lambda event, index=number_button: self.left_click(event, index))
                    self.buttons[number_button].bind("<Button-1>", lambda event, item=item: self.right_click(event, item))
                    

                    self.index = [number_button]
                    self.bomb_index.append(self.buttons[number_button])
                    self.bomb_index2.append(number_button)



                if item == 0:
                    self.buttons.append(Label(self.frame1, text="-",  image=self.empty))
                    self.buttons[number_button].bind("<Button>", lambda event, index=number_button: self.left_click(event, index))
                    self.buttons[number_button].bind("<Button-1>", lambda event, item=item: self.right_click(event, item))
                    

                    self.index = [number_button]



                if item != "B" and item != 0:
                    self.buttons.append(Label(self.frame1, text="-",  image=self.empty))
                    self.buttons[number_button].bind("<Button>", lambda event, index=number_button: self.left_click(event, index))
                    self.buttons[number_button].bind("<Button-1>", lambda event, item=item: self.right_click(event, item))
                    
                    
                    self.index = [number_button]


                self.buttons[number_button].grid(row=key, column=colum_index+1)
                number_button += 1
            

        
        self.root.mainloop()

            

    def left_click(self, event, index):
        """
        A function to put and remove a flag on a unrevealed field.

        :param event: Given Label.
        :type event: object
        """

        value = event.widget.cget("text")

        if value != "flag":
            event.widget.configure(text="flag",  image=self.flag)
            
            self.flag_counter-=1
            self.flag_shower.config(text=self.flag_counter)

            self.flag_index.append(index)

            self.game_won() #check if all flags are positioned well


        if value == "flag":
            event.widget.configure(text="-",  image=self.empty)

            self.flag_counter+=1
            self.flag_shower.config(text=self.flag_counter)

            self.flag_index.remove(index)



    def right_click(self, event, item):
        """
        A function to reveal a unvrealed field.

        :param event: Given Label.
        :type event: object

        :param item: Holding item of a field.
        :type item: int or str
        """
        if item == 0:
            event.widget.configure(text=item,  image=self.revealed)
        
        if item == 1:
            event.widget.configure(text=item,  image=self.one)

        if item == 2:
            event.widget.configure(text=item,  image=self.two)

        if item == 3:
            event.widget.configure(text=item,  image=self.three)

        if item == 4:
            event.widget.configure(text=item,  image=self.four)

        if item == 5:
            event.widget.configure(text=item,  image=self.five)

        if item == 6:
            event.widget.configure(text=item,  image=self.six)

        if item == 7:
            event.widget.configure(text=item,  image=self.seven)

        if item == 8:
            event.widget.configure(text=item,  image=self.eight)

        if item == "B":
            event.widget.configure(text=item,  image=self.bomb)
            self.reveal_all()
            self.explode_all_bombs()
            self.open_retry_window("You lose!")


        event.widget.unbind("<Button>")
        event.widget.unbind("<Button-1>")
        




    def explode_all_bombs(self):
        """
        A function to reveal all bombs in the game field after the user caught one bomb.
        """

        for bomb in self.bomb_index:
            bomb.config(text="B", image=self.bomb)

    def reveal_all(self):
        """
        A function to unbind all Label in the game field after the game is finished.
        """

        for label in self.buttons:
            label.unbind("<Button>")
            label.unbind("<Button-1>")


    def game_won(self):
        """
        A function to check if user placed all flags correctly.
        """
        self.flag_index.sort()
        
        if self.flag_index == self.bomb_index2:
            self.reveal_all()
            self.open_retry_window("You won!")




    def open_retry_window(self, text):
        """
        A function to ask the user to continue the game. A own window will be displayed.
        """
        self.root2 = Tk()
        self.root2.geometry("200x200")

        label = Label(self.root2, text=text)
        label.pack()

        label2 = Label(self.root2, text="What do you want do?")
        label2.pack()

        retry = Button(self.root2, text="Retry", command=self.yes_retry)
        retry.pack()

        retry2 = Button(self.root2, text="Exit", command=self.no_retry)
        retry2.pack()
        self.root2.mainloop()



    def yes_retry(self):
        """
        A function for a button from retry window. This function will close the application if the user doesn't want to continue.
        """
        self.root2.destroy()
        self.root.destroy()



    def no_retry(self):
        """
        A function for a button from retry window. This function will close the application and restart the game if the user wants to continue.
        """
        self.status = True
        self.root2.destroy()
        self.root.destroy()

    def exit(self):
        """
        A function to close application.
        """
        
        self.status = True
        self.root.destroy()
        



    def resized(self, path):
        """
        A function to resize the loaded image to a given size.

        :param path: Given path to image.
        :type path: str
        """
        pic = Image.open(path)
        resized = pic.resize((50, 50), Image.ANTIALIAS)

        return ImageTk.PhotoImage(resized)
    



