from JeuSequentiel import JeuSequentiel
from Strategie import Strategie

import random

class StrategieAleatoire(Strategie):    
    """
    Represente une strategie de jeu aleatoire pour tout jeu sequentiel
    """
    def __init__(self, jeu: JeuSequentiel):
        super().__init__(jeu)

    def choisirProchainCoup(self, C):
        """
        Choisit un coup aleatoire suivant une distribution uniforme sur tous les coups possibles
        dans la configuration C
        """
        return random.choice(C.coupsPossibles())