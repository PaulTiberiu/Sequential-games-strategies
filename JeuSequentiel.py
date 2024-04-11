class JeuSequentiel:
    """Represente un jeu sequentiel, a somme
    nulle, a information parfaite"""
    def __init__(self):
        pass

    def joueurCourant(self, C):
        """Rend le joueur courant dans la
        configuration C"""
        raise NotImplementedError

    def coupsPossibles(self, C):
        """Rend la liste des coups possibles dans
        la configuration C"""
        return C.coupsPossibles()

    def f1(self, C):
        """Rend la valeur de l'evaluation de la configuration C pour le joueur 1"""
        raise NotImplementedError

    def joueLeCoup(self, C, coup):
        """Rend la configuration obtenue apres que le joueur courant ait joue le coup
        dans la configuration C"""
        raise NotImplementedError

    def estFini(self, C):
        """ Rend True si la configuration C est
        une configuration finale"""
        return C.estFinale()

    def prochaine_configuration(self, C, coup):
        raise NotImplementedError
