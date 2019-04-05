from person import Person
from board import bd
from mario import mar
import numpy as np


class Enemy(Person):
    def __init__(self, r, c):
        Person.__init__(self, r, c)
        self.random_prob = 0.6
        self.pmo=[0, 3]

    def move(self):
        if bd.canvas[self.r, self.c] < 5:
            bd.canvas[self.r, self.c] = 0
        dr = [0, 0]
        dc = [1, -1]
        if np.random.random_sample() < self.random_prob:
            rand = np.random.randint(2)
            if self.check_move(dr[rand], dc[rand]):
                self.r = self.r + dr[rand]
                self.c = self.c + dc[rand]
        else:
            dz = self.best_direction()
            self.r = self.r + dz[0]
            self.c = self.c + dz[1]
        
        bd.canvas[self.r, self.c] = 4
    
    def moverel(self,c):
        if bd.canvas[self.r, self.c] < 5:
            bd.canvas[self.r, self.c] = 0
        if self.check_move(0, c):
                self.c = self.c + c
                        
        bd.canvas[self.r, self.c] = 4

    def best_direction(self):
        dr = [0, 0 ]
        dc = [1, -1 ]
        manhattan_dis = 10000
        final_dir = [0, 0]
        for pos in range(2):
            if self.check_move(dr[pos], dc[pos]):
                cur_dis = abs(mar.r - self.r - dr[pos]) + abs(mar.c - self.c - dc[pos])
                if cur_dis <= manhattan_dis:
                    manhattan_dis = cur_dis
                    final_dir = [dr[pos], dc[pos]]
        return final_dir
