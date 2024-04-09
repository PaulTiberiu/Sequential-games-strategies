from JeuSequentiel import JeuSequentiel

class Strategie():
    """
    Represente une strategie de jeu
    """

    def __init__(self, jeu: JeuSequentiel):
        self.jeu = jeu

    def choisirProchainCoup(self, C):
        """
        Choisit un coup parmi les coups possibles dans la configuration C
        """
        raise NotImplementedError
    
