from person import Person
from board import bd
from config import ROWS, COLUMNS
import time


class Mario(Person):
    def __init__(self, r, c):
        Person.__init__(self, r, c)
        self.lives = 3
        self.num_bombs = 1
        self.pmo=[ 0 ,3 , 4 ]
        self.abpos=c

    """
        This method checks if a given moves is valid or not.
        Parent method has been overridden in this class
    """

    """
        To move the Bomberman in whichever direction the user requires when possible
    """

    def move_sc(self,dr,dc):
        return ( dc>0 and self.abpos < (COLUMNS-2)/2 ) or ( dc < 0 and self.abpos <=  (COLUMNS-2)/2 ) or self.abpos > 150       

    def move(self, dr, dc):
        if self.check_move(dr, dc):
            if bd.canvas[self.r, self.c] <= 5:
                 bd.canvas[self.r, self.c] = 0
            self.r = self.r + dr
            if self.move_sc(dr,dc):
                self.c = self.c + dc
            self.abpos = self.abpos + dc


mar = Mario(ROWS-2, 1)
