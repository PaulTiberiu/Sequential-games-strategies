from Coup import Coup

class CoupMorpion(Coup):
    def __init__(self, joueur, x, y):
        super().__init__(joueur)
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def position(self):
        return self.get_x(), self.get_y()
    
    def __repr__(self):
        return f"({self.get_x()},{self.get_y()})"