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

    # def negamax(self, C, profondeur, maximise):
    #     if profondeur == self.profondeur_max:
    #         return 0, C.getDernierCoup()
    #
    #     if self.jeu.estFini(C):
    #         return C.f1_geek() * 1 if maximise else - 1, C.getDernierCoup()
    #
    #     valeur_actuelle = float('-inf')
    #     coup_actuel = None
    #
    #     for coup in self.jeu.coupsPossibles(C):
    #         prochaine_config = self.jeu.prochaine_configuration(C, coup)
    #
    #         valeur, cpa = self.negamax(prochaine_config, profondeur + 1, not maximise)
    #         #print(valeur)
    #
    #         valeur = -valeur
    #         if valeur > valeur_actuelle:
    #             valeur_actuelle = valeur
    #             coup_actuel = coup
    #     return valeur_actuelle, coup_actuel
    #
    #
    # def prepare_negamax(self, C):
    #     maximise = True if self.jeu.joueurCourant(C) == 1 else False
    #     val, coup = self.negamax(C, 0, maximise)
    #     return coup


    def minimax(self, C, profondeur, maximise):
        coupsPossibles = self.jeu.coupsPossibles(C)
        meilleur_coup = None


        if profondeur == 0 or coupsPossibles == []:
            return C.f1_geek(), None

        if maximise:
            meilleur_score = float("-inf")
            for coup in coupsPossibles:
                config_suivante = self.jeu.prochaine_configuration(C, coup)
                m_score, m_coup = self.minimax(config_suivante, profondeur - 1, False)
                meilleur_score = max(meilleur_score, m_score)
                if meilleur_score == m_score:
                    meilleur_coup = coup

            return meilleur_score, meilleur_coup

        else:
            meilleur_score = float("inf")

            for coup in coupsPossibles:
                config_suivante = self.jeu.prochaine_configuration(C, coup)
                m_score, m_coup = self.minimax(config_suivante, profondeur - 1, True)
                meilleur_score = min(meilleur_score, m_score)
                if meilleur_score == m_score:
                    meilleur_coup = coup

            return meilleur_score, meilleur_coup




    def choisirProchainCoup(self, C):
        #coup = self.prepare_negamax(C)
        maximise = self.jeu.joueurCourant(C) == 1
        val, coup = self.minimax(C, 9, maximise)
        return coup

    # def choisirProchainCoup(self, C):
    #     """
    #     Choisit le prochain coup en utilisant l'algorithme MinMax
    #     """
    #     meilleur_coup = None
    #     meilleur_valeur = float('-inf')
    #
    #     #maximise = True if self.jeu.joueurCourant(C) == 1 else False
    #
    #     minimise = True if self.jeu.joueurCourant(C) == 1 else False
    #
    #     for coup in self.jeu.coupsPossibles(C):
    #         valeur = self.negamax(C, coup, 0, minimise)
    #         print(valeur)
    #         if valeur > meilleur_valeur:
    #             meilleur_valeur = valeur
    #             meilleur_coup = coup
    #
    #     return meilleur_coup



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


    # def negamax(self, C, coup, profondeur, minimise):
    #     config_actuelle = self.jeu.prochaine_configuration(C, coup)
    #
    #     if profondeur == self.profondeur_max or self.jeu.estFini(config_actuelle):
    #         return config_actuelle.f1_geek() if not(minimise) else - config_actuelle.f1_geek()
    #
    #
    #     meilleur_valeur = float('-inf')
    #
    #     for prochain_coup in self.jeu.coupsPossibles(config_actuelle):
    #         valeur = self.negamax(config_actuelle, prochain_coup, profondeur+1)
    #         meilleur_valeur = max(meilleur_valeur, valeur) if config_actuelle.prochainJoueur() == 1 else max(meilleur_valeur, - valeur)
    #     return meilleur_valeur