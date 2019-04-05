from board import bd
from mario import mar
import helper
from enemy import Enemy
from config import LIVES_1, LIVES_2, WIN, GAME_OVER, LEVEL_1
import numpy as np
import os
import time
from colorama import Fore, Back, Style
from time import sleep
import entity as en

input=helper.KBHit()

class Game:

    """
        A function to render (Print) the board.
    """

    def render(self):
        os.system('clear')
        print("Score: ", bd.score, " Lives: ", mar.lives, " Level: ", bd.level )
        board_mapping = {
            0: '    ',
            2: '****',
            5: 'XXXX'  
                  }
        """
            This loop is responsible for mapping the canvas to game_board
        """
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] == 3:
                    bd.canvas[row, col]=0
                if mar.r == row and mar.c == col:
                    bd.canvas[row, col]=3
                    bd.game_area[2*row][col] = "[^^]"
                    bd.game_area[2*row+1][col] = " ][ "
                elif bd.canvas[row, col] == 4:
                    for enemy in bd.enemies:
                        if enemy.r == row and enemy.c == col:
                            if enemy.__class__.__name__ == "Enemy":
                                bd.game_area[2*row][col] = "<**>"
                                bd.game_area[2*row+1][col] =" () "
                else:
                    bd.game_area[2*row][col] = board_mapping[bd.canvas[row, col]]
                    bd.game_area[2*row+1][col] = board_mapping[bd.canvas[row, col]]

        self.__vertical_border()
        self.__vertical_border()
        for row in range(2*bd.rows):
            print('###', end='',sep='')
            for col in range(bd.columns):
                if bd.game_area[row][col] == "[^^]" or bd.game_area[row][col] == "<**>" or bd.game_area[row][col] == "()":
                     print(Fore.RED+bd.game_area[row][col], end='',sep='')
                elif  bd.game_area[row][col] == " ][ ":
                     print(Fore.WHITE+bd.game_area[row][col], end='',sep='')                   
                elif bd.game_area[row][col] == "****":
                     print(Fore.GREEN+bd.game_area[row][col] , end='',sep='')
                elif bd.game_area[row][col] == "XXXX":
                     print(Fore.WHITE+bd.game_area[row][col] , end='',sep='')
                else :
                     print(bd.game_area[row][col], end='',sep='')
            print('###')
        self.__vertical_border()
        self.__vertical_border()

        # for row in range(bd.rows):
        #     for col in range(bd.columns):
        #         print(bd.canvas[row][col],end='')
        #     print('\n')


    @staticmethod
    def __vertical_border():
        print('###', end='',sep='')
        for col in range(4*bd.columns):
            print('#', end='',sep='')
        print('###')

    @staticmethod
    def game_over():
        os.system('clear')
        print(GAME_OVER)
        time.sleep(2)
        print("Oops, you died. Your final score is: ", bd.score)
        time.sleep(1)
        exit()

    @staticmethod
    def game_win():
        os.system('clear')
        print(WIN)
        time.sleep(2)
        print("You Won !!!! Your final score is: ", bd.score)
        time.sleep(1)
        exit()


    @staticmethod
    def create_enemies():
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] == 4:
                    if bd.level == 1:
                        bd.enemies.append(Enemy(row, col))


    @staticmethod
    def decrease_lives():
        os.system('clear')
        mar.lives -= 1
        if mar.lives == 1:
            print(LIVES_1)
        elif mar.lives == 2:
            print(LIVES_2)
        time.sleep(2)
        bd.canvas[mar.r, mar.c] = 0
        bd.canvas[0, 0] = 3
        mar.r = 0
        mar.c = 0
        mar.abpos=0
        for row in range(bd.rows):
            for col in range(bd.columns):
                if bd.canvas[row, col] >= 5:
                    bd.canvas[row, col] = 0

    @staticmethod
    def reinitialize_board():
        bd.game_area = [["aaaa" for i in range(bd.columns)] for j in range(2 * bd.rows)]
        bd.enemies = []
        bd.canvas = np.zeros((bd.rows, bd.columns))
        bd.fillcanvas()
        game.create_enemies()
        mar.r = 0
        mar.c = 0
        mar.abpos=0
        os.system('clear')
    
    def keych(self,key):
            if key == 'a':
                if mar.c > 0:

                        mar.move(0, -1)
                        if not mar.move_sc(0,-1):
                           for en in bd.entities:
                               en.move(1)

            elif key == 'd':
                if mar.c < bd.columns:

                    
                        mar.move(0, 1)
                        if not mar.move_sc(0,1):
                           for en in bd.entities:
                               en.move(-1)
                           for en in bd.enemies:
                               en.moverel(-1)

            elif key == 'q':
                self.game_over()

    def game_loop(self):

        
        jumpfl=0
        while True:
            self.render()
            
            if jumpfl :
                  for i in range(1,4):
                    start=time.perf_counter()
                    while(start+0.05*i>time.perf_counter()):
                        if input.kbhit():
                          self.keych(input.getch())
                    mar.move(-1,0)
                    self.render()
                  jumpfl=0
               
            while mar.check_move(1, 0) and jumpfl == 0:
               for i in range(1,-4,-1):
                   if i<1:
                      i=1
                   start=time.perf_counter()
                   while(start+0.01*i>time.perf_counter()):
                      if input.kbhit() :
                         self.keych(input.getch())
                   for enemy in bd.enemies:
                      if enemy.r == mar.r + 1 and enemy.c == mar.c:
                       bd.score += 100
                       bd.canvas[enemy.r, enemy.c] = 0
                       bd.enemies.remove(enemy)
                   mar.move(1,0)
                   self.render()


            key = input.getch()
            if key == 'w':
                if mar.r > 0:
                    jumpfl=1
            self.keych(key)
           

            for enemy in bd.enemies:
                enemy.fall()
                enemy.move()
                if enemy.r == mar.r and enemy.c == mar.c:
                    if mar.lives > 1:
                        self.decrease_lives()
                    else:
                        self.game_over()

            if [mar.r, mar.c] in bd.enemies:
                if mar.lives > 1:
                    self.decrease_lives()
                else:
                    self.game_over()



game = Game()
beginning_time = time.time()
bd.entities.append(en.Stairs(bd.rows - 1,bd.columns-3,6))
game.create_enemies()
print(LEVEL_1)
time.sleep(2)
game.game_loop()
