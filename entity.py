from board import bd
import numpy as np


def m0(x):
    return max( 0 , x )

class Entity:
    def __init__(self, r, c):
        self.r = r
        self.c = c     
    """
        An abstract method which is overridden by the children classes
    """
    def move(self,dc):
        pass

class Stairs(Entity):

    def __init__(self,r,c,n):
        Entity.__init__(self,r,c)
        self.sz=n
        self.STAIR=self.stairsz(n)
        bd.canvas[self.r - self.sz : self.r , self.c - self.sz : self.c]=self.STAIR

    def move(self,dc):
        print(bd.canvas[self.r - 1, self.c + dc - 5],' ',self.r,' ',self.c + dc )
        if (dc<0 and bd.canvas[self.r - 1, self.c + dc - 4] in [ 0 , 2 ,5 ]) or (dc>0 and bd.canvas[self.r - 1, self.c + dc + 1] in [ 0 , 2 ,5 ]):
            bd.canvas[self.r-self.sz : self.r , m0(self.c - self.sz) : m0(self.c)]=np.zeros((self.sz, - m0(self.c - self.sz) + m0(self.c)))
            self.c = self.c + dc
            bd.canvas[self.r-self.sz : self.r , m0(self.c - self.sz) : m0(self.c)]=self.STAIR[ 0:self.sz, self.sz + m0(self.c - self.sz) - m0(self.c):self.sz  ]

    def stairsz(self,n):
        STAIRS = np.full((n, n),5)
        for i in range(n) :
            for j in range(n):
                if j <= n - i:
                    STAIRS[i,j] = 0

        return STAIRS

