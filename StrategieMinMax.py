from JeuSequentiel import JeuSequentiel
from Strategie import Strategie 
from CoupMorpion import CoupMorpion


class StartegieMinMax(Strategie):
    """
    Represente une strategie utilisant un arbre min-max de profondeur k
    """

    def __init__(self, jeu: JeuSequentiel, k: int):
        super().__init__(jeu)
        self.profondeur_max = k

    def choisirProchainCoup(self, C):
        """
        Choisit le prochain coup en utilisant l'algorithme MinMax
        """
        meilleur_coup = None
        meilleur_valeur = float('-inf')
        
        maximise = True if self.jeu.joueurCourant(C) == 1 else False

        for coup in self.jeu.coupsPossibles(C):
            valeur =  self.negamax(C, CoupMorpion(C.prochainJoueur(), *coup.position()), 0, maximise)
            
            print(valeur)
            if valeur > meilleur_valeur:
                meilleur_valeur = valeur
                meilleur_coup = coup
            
        return meilleur_coup

        
        
    # def min_max(self, C, coup, profondeur, est_joueur_maximisant):
    #     if profondeur == self.profondeur_max or self.jeu.estFini(C):
    #         return C.f1() if est_joueur_maximisant else - C.f1()

    #     if est_joueur_maximisant:
    #         meilleur_valeur = float('-inf')
    #         prochaine_config = self.jeu.prochaine_configuration(C, coup)

    #         for prochain_coup in self.jeu.coupsPossibles(prochaine_config):
    #             valeur = self.min_max(prochaine_config, prochain_coup, profondeur+1, False)
    #             meilleur_valeur = max(meilleur_valeur, valeur)
    #         return meilleur_valeur
        
    #     else:
    #         meilleur_valeur = float('inf')
    #         prochaine_config = self.jeu.prochaine_configuration(C, coup)

    #         for prochain_coup in self.jeu.coupsPossibles(prochaine_config):

    #             valeur = self.min_max(prochaine_config, prochain_coup, profondeur+1, True)
    #             meilleur_valeur = min(meilleur_valeur, valeur)
    #         return meilleur_valeur

        
    def negamax(self, C, coup, profondeur, est_joueur_maximisant):
        
        if profondeur == self.profondeur_max or self.jeu.estFini(C):
            return C.f1_geek() if est_joueur_maximisant else - C.f1_geek()

        
        meilleur_valeur = float('-inf')
        config_actuelle = self.jeu.prochaine_configuration(C, coup)
        for prochain_coup in self.jeu.coupsPossibles(config_actuelle):
            valeur = - self.negamax(config_actuelle, CoupMorpion(C.prochainJoueur(), *prochain_coup.position()), profondeur+1, not(est_joueur_maximisant))
            meilleur_valeur = max(meilleur_valeur, valeur)
        return meilleur_valeur