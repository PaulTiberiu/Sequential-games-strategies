from Configuration import Configuration
from copy import deepcopy
from CoupAllumettes import CoupAllumettes
from Graph import Graph

class ConfigurationAllumettes(Configuration):

    def __init__(self, tab_m, g):
        super().__init__()   
        assert len(tab_m) == g
        self.groupes = tab_m

    def __repr__(self):
        return ' | '.join([str(groupe) for groupe in self.groupes])

    def __eq__(self, other) -> bool:
        return self.groupes == other.groupes
    
    def __hash__(self) -> int:
        return hash(tuple(self.groupes))
    
    def __lt__(self, other):
        return sorted(self.groupes) < sorted(other.groupes)
    
    def prochainJoueur(self):
        if self.historique == [] or self.getDernierCoup().get_joueur() == 2:
            return 1
        elif self.getDernierCoup().get_joueur() == 1:
            return 2   
        raise ValueError

    # def coupsPossibles(self):
    #     """
    #     Renvoie la liste des coups possibles dans la configuration C
    #     """
    #     coups = []
    #     for i, groupe in enumerate(self.groupes):
    #         if groupe > 0:
    #             # Pour chaque groupe restant, les coups possibles sont de retirer 1 a groupe jusqu'a 0
    #             for j in range(1, groupe + 1):
    #                 coups.append(CoupAllumettes(self.prochainJoueur(), j, i)) # (indice du groupe, nb d'allumettes a retirer)

    #     return coups

    def coupsPossibles(self):
        """
        Renvoie la liste des coups possibles dans la configuration C
        """
        coups = []
        for i, groupe in enumerate(self.groupes):
            if groupe > 0:
                # Pour chaque groupe restant, les coups possibles sont de retirer 1 a groupe jusqu'a 0
                for j in range(1, groupe + 1):
                    if j <= 3:
                        coups.append(CoupAllumettes(self.prochainJoueur(), j, i)) # (indice du groupe, nb d'allumettes a retirer)

        return coups
    
    def f1(self):
        g = Graph.create_graph(self)
        
        return g.grundyOf(self)
    

  

    def joueLeCoup(self, coup):
        """
        Renvoie la configuration obtenue apres que le joueur courant ait joué le coup dans la configuration C.
        """
        groupe, nb_allumettes = coup.position(), coup.get_count()
        self.groupes[groupe] -= nb_allumettes
        
        
        self.historique.append(coup)
        
        return self.groupes
        
    def prochaine_configuration(self, coup):
        """renvoie la prochaine configuration si le coup est joué"""
        
        cp = deepcopy(self)
        cp.joueLeCoup(coup)
        return cp

    def estFinale(self):
        return all(groupe == 0 for groupe in self.groupes)


