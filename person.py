from board import bd

class Person:
    

    def __init__(self, r, c):
        self.r = r
        self.c = c  
        self.pmo=[0]
    """
        An abstract method which is overridden by the children classes
    """
    def move(self):
    	pass

    def check_move(self, dr, dc):
        if 0 <= self.r + dr < bd.rows and 0 <= self.c + dc < bd.columns:
            if bd.canvas[self.r + dr, self.c + dc] in self.pmo:
                return True
            return False
        return False

    def fall(self):
    	fb = self.check_move(1,0)
    	if self.check_move(1,0):
    		self.r += 1
    	return fb



