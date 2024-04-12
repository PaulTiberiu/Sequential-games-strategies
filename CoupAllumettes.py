from Coup import Coup

class CoupAllumettes(Coup):
    def __init__(self, joueur, count, row):
        super().__init__(joueur)
        self.count = count
        self.row = row

    def get_row(self):
        return self.row
    
    def get_count(self):
        return self.count
    
    def position(self):
        return self.get_row()
    
    def __repr__(self):
        return f"joueur {self.get_joueur()} : row {self.position()}, count = {self.get_count()}"