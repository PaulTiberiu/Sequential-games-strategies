from JeuSequentiel import JeuSequentiel
from Strategie import Strategie 
from CoupAllumettes import CoupAllumettes
from random import choice

from Graph import Graph

class StrategieGrundy(Strategie):


    def __init__(self, jeu: JeuSequentiel, C):
        self.jeu = jeu
        self.graph = self.precompute_graph(C)

    def choisirProchainCoup(self, C):
        coups = []
        
        for coup in C.coupsPossibles():
            config = C.prochaine_configuration(coup)
            if not config.estFinale():
                grundy = self.graph.grundyOf(config)

                if grundy == 0:
                    return coup
        
            coups.append(coup)
        
        return choice(coups)
    
    def precompute_graph(self, C):
        return Graph.create_graph(C)
