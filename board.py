from config import ROWS, COLUMNS
import numpy as np

"""
    The Board class represents the state of the board.
        0   => Air
        2   => Ground
        3   => Mario
        4   => Enemies
        5   => Stairs
"""


class Board:
    """
        Constructor of Board class. 
        
        canvas => A numpy 2D matrix of integers which represent different characters
                  It represents the current state of game
        game_area => A list of list which is used for rendering the game
        enemies => A list of objects storing all the instances of various enemies in the board
        entities => A list of objects storing all the instances of various entities like Stairs.. in the board
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.canvas = np.zeros((rows, columns))
        self.game_area = [["aaaa" for i in range(columns)] for j in range(2*rows)]
        self.enemies = []
        self.entities = []
        self.score = 0
        self.level = 1

    """
        Fills the canvas (Game Matrix) with all the characters
    """

    def fillcanvas(self):
        for i in range(self.rows-2,self.rows):
            for j in range(self.columns):
                if i==self.rows-2 :
                    if j==1:
                        self.canvas[i, j] = 3
                else :
                        self.canvas[i, j] = 2

                if i==self.rows-2 and j==self.columns-10:
                        self.canvas[i,j]=4

bd = Board(ROWS, COLUMNS)
bd.fillcanvas()
