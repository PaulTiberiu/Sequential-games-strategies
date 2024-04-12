from JeuSequentiel import JeuSequentiel

class Allumettes(JeuSequentiel):
    """
    Represente le jeu des allumettes avec g groupes de m allumettes chacun.
    """

    def __init__(self):
        super().__init__()


    def joueurCourant(self, C):
        """"
        Rend le joueur courant dans la configuration C
        """
        return C.prochainJoueur()

    def coupsPossibles(self, C):
        """
        Renvoie la liste des coups possibles dans la configuration C
        """
        return C.coupsPossibles()
    
    def f1(self, C):
        return C.f1()

    def joueLeCoup(self, C, coup):
        """
        Renvoie la configuration obtenue apres que le joueur courant ait joue le coup dans la configuration C.
        """
        groupe, nb_allumettes = coup
        self.groupes[groupe] -= nb_allumettes
        return self.groupes
    
    def estFinale(self, C):
        return C.estFinale()    

    def joueurCourant(self, C):
        """"
        Rend le joueur courant dans la configuration C
        """
        return C.prochainJoueur()
    
    def prochaine_configuration(self, C, coup):
        return C.prochaine_configuration(coup)