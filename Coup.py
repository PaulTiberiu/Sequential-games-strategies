

class Coup:
    def __init__(self, joueur):
        self.joueur = joueur

    def get_joueur(self):
        return self.joueur

    def position(self):
        raise NotImplementedError