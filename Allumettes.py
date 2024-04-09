from JeuSequentiel import JeuSequentiel

class Allumettes(JeuSequentiel):
    """
    Represente le jeu des allumettes avec g groupes de m allumettes chacun.
    """

    def __init__(self, m, g):
        super().__init__()
        self.groupes = [m] * g

    def joueurCourant(self, C):
        """"
        Rend le joueur courant dans la configuration C
        """
        pass

    def coupsPossibles(self, C):
        """
        Renvoie la liste des coups possibles dans la configuration C
        """
        coups = []
        for i, groupe in enumerate(self.groupes):
            if groupe > 0:
                # Pour chaque groupe restant, les coups possibles sont de retirer 1 a groupe jusqu'a 0
                for j in range(1, groupe + 1):
                    coups.append((i, j)) # (indice du groupe, nb d'allumettes a retirer)
        return coups
    
    def f1(self, C):
        pass

    def joueLeCoup(self, C, coup):
        """
        Renvoie la configuration obtenue apres que le joueur courant ait joue le coup dans la configuration C.
        """
        groupe, nb_allumettes = coup
        self.groupes[groupe] -= nb_allumettes
        return self.groupes
    
    def estFini(self, C):
        return all(groupe == 0 for groupe in self.groupes)
    

    

        
        
        


