from JeuSequentiel import JeuSequentiel
from Strategie import Strategie 
from CoupAllumettes import CoupAllumettes
from random import choice

from Graph import Graph

class StrategieGrundyOpti(Strategie):


    def __init__(self, jeu: JeuSequentiel):
        self.jeu = jeu

    def choisirProchainCoup(self, C):
        coups = []
        
        for coup in C.coupsPossibles():
            config = C.prochaine_configuration(coup)

            if not config.estFinale():
                graph = self.compute_graph(config)
                grundy = graph.getGrundyMulti(config)

                if grundy == 0:
                    return coup
        
            coups.append(coup)
        
        return choice(coups)
    
    def compute_graph(self, C):
        tab_m = C.groupes
        group_graphs = Graph.create_group_graphs(tab_m)

        product = group_graphs[0]

        for i in range(1, len(group_graphs)):
            product = Graph.cartesian_sum(product, group_graphs[i])
        
        final = Graph.final_graph(product)

        return final

