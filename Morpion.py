from JeuSequentiel import JeuSequentiel
from CoupMorpion import CoupMorpion
from ConfigurationMorpion import ConfigurationMorpion
from StrategieAleatoire import StrategieAleatoire


class Morpion(JeuSequentiel):
    """
    Represente un jeu de morpion (3x3)
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
        """
        Renvoie l'évaluation de la configuration obtenue apres que le joueur courant ait joué le coup dans la configuration C.
        """
        C.f1()
        
    def joueLeCoup(self, C, coup):
        """
        Renvoie la configuration obtenue apres que le joueur courant ait joue le coup dans la configuration C.
        """
        i, j = coup.position()
        joueur = self.joueurCourant(C)

        c = CoupMorpion(joueur, i ,j)
        return C.jouer_coup(c)
    
    def prochaine_configuration(self, C, coup):
        return C.prochaine_configuration(coup)
    
    def estFinale(self, C):
        """
        Renvoie True si la configuration C est une configuration finale
        """
        #' ' not in [cell for row in self.grille for cell in row]
        return C.estFinale()
    
    def estGagnant(self, C,  joueur):
        """
        Verifie si le joueur donne a gagne dans la configuration actuelle.
        """
        return C.estGagnant(joueur)

    def jouerPartie(self, C, strategie, *args):
        st = strategie.__new__(strategie)
        st.__init__(self, *args)

        print("debut")

        while not(self.estFinale(C)):
           
           # joueur = 1
            coup = st.choisirProchainCoup(C)
            self.joueLeCoup(C, coup)

            print(C)

            if self.estFinale(C) : break
        
            #joueur = 2
            coup = st.choisirProchainCoup(C)
            self.joueLeCoup(C, coup)

            print(C)
