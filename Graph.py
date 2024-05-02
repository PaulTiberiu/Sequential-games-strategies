from Vertex import Vertex
from ConfigurationAllumettes import ConfigurationAllumettes
from CoupAllumettes import CoupAllumettes

class Graph:
    V = set # Ensemble de sommets (la liste de sommets) 
    E = dict # Dictionnaire de arcs avec les poids (la liste d'arretes)
    
    def __init__(self, V, E=None):
        """
        Permet de creer le graphe avec les valeurs V et E pasees en parametre
        """
        
        self.V = V
        self.grundy = None
        if(E == None):
            self.E = {i.id : set() for i in V} # Creer le dictionnaire qui relie le sommet i a vide
        else:
            self.E = E

    def __str__(self) -> str:
        return str([v for v in self.V])

    def grundyOf(self, conf):
        res = {c:0 for c in self.V}
        
        for k in res.keys():
            if k == Vertex(conf):
                return k.grundy

        raise ValueError("T")
    
    def __repr__(self) -> str:
        return str([v for v in self.V])

    def insert_edge(self, v1, v2): 
        """
        Permet d'ajouter une arrete
        """

        self.E[v1].add(v2)

    def getEdges(self):
        ret = ""
        for k, v in sorted(self.E.items()):
            ret = ret + str(k) + " grundy = "+ str(self.grundyOf(k)) + "  ->  " + str(sorted(v, reverse=True)) +'\n'
        return ret

    def getGrundiesEdges(self):
        ret = ""
        for k, v in sorted(self.E.items()):
            ret = ret + str(k) + " grundy = "+ str(self.grundyOf(k)) + "  ->  " + str(sorted([self.grundyOf(vx) for vx in v])) +'\n'
        return ret

    def grundys(self):
        return '\n'.join([ str(v) for v in self.V])

    def grundys_eq(self, val):
        return '\n'.join([ str(v) for v in self.V if v.grundy == val])
    

    def compute_all_grundys(self):
        while not self.all_grundys_set():
            
            for vertex in self.V:
                if vertex.grundy == None and all( self.getVertex(child).grundy != None for child in self.E[vertex.id]):
                    self.compute_grundy(vertex)

            
    def getVertex(self, id):
        for v in self.V:
            if v.id == id:
                return v
        raise ValueError
    
    def all_grundys_set(self):
        return all( vertex.grundy != None for vertex in self.V)
    
    def compute_grundy(self, vertex):
        grundy = 0
        changed = True

        while changed :
            changed = False
            for child in self.E[vertex.id]:
                if self.getVertex(child).grundy == grundy:
                    grundy = grundy + 1
                    changed = True
                    continue
          
        vertex.setGrundy(grundy)

    @staticmethod
    def create_graph(configuration):

        edges = {}
        edges[configuration] = set()
        vertexes = set([Vertex(configuration)])

        Graph.complete_graph(configuration, vertexes, edges)
        g = Graph(vertexes, edges)

        g.compute_all_grundys()
        return g

    @staticmethod
    def complete_graph(conf, vertexes, edges):

        if edges.get(conf) == None:
            edges[conf] = set()

        for c in conf.coupsPossibles():
            new = conf.prochaine_configuration(c)
            if not new.estFinale():
                v = Vertex(new)

                vertexes.add(v)

                
                edges[conf].add(new)
                Graph.complete_graph(new, vertexes, edges)


    @staticmethod
    def cartesian_sum(G1, G2):
        X = set()
        for vertex1 in G1.V:
            #print("Vertex1:", vertex1.id)
            #print("G1.E:", G1.E[vertex1.id])

            for vertex2 in G2.V:
                new_vertex_id = str(vertex1.id) + "-" + str(vertex2.id)
                X.add(Vertex(new_vertex_id))

        L = dict()
        for vertex1 in G1.V:
            for vertex2 in G2.V:
                key = str(vertex1.id) + "-" + str(vertex2.id)
                L[key] = set()

        print("X:", X)
        print("L:", L)

        print("G1.V:", G1.V)
        print("G2.V:", G2.V)

        print("G1.E:", G1.E)
        print("G1.E:", G1.E[1])
        print("G2.E:", G2.E)

        for vertex in X:
            vertex1_id, vertex2_id = vertex.id.split("-")
            print("Vertex1:", vertex1_id, " Vertex2:", vertex2_id)

            print("G1.E:", G1.E[int(vertex1_id)])

            for child1 in G1.E[vertex1_id]:
                #print("Child1:", child1)
                L[vertex.id].add(child1 + "-" + vertex2_id)

            for child2 in G2.E[vertex2_id]:
                #print("Child2:", child2)
                L[vertex.id].add(vertex1_id + "-" + child2)

        G = Graph(X, L)
        return G
    
    @staticmethod
    def digital_sum(p, q):
        # Convertir p et q en binaire
        p_binary = bin(p)[2:]
        q_binary = bin(q)[2:]

        # Avoir la meme longueur pour faire la somme bit a bit
        max_length = max(len(p_binary), len(q_binary))
        p_binary = p_binary.zfill(max_length)
        q_binary = q_binary.zfill(max_length)

        # Calculer la somme digitale
        digital_sum = int(p_binary, 2) ^ int(q_binary, 2)

        return digital_sum
    
    # @staticmethod
    # def create_game_graph(tab_m, conf):
    #     group_graphs = Graph.create_group_graphs(tab_m)

    #     print("Group Graphs:", group_graphs)

    #     game_graph = group_graphs[0]
    #     grundy_game_graph = game_graph.grundyOf(conf)

    #     for graph in group_graphs[1:]:
            
    #         grundy_graph = graph.grundyOf(graph, conf)
    #         game_graph = Graph.cartesian_sum(graph, game_graph)
    #         grundy_game_graph = Graph.digital_sum(grundy_game_graph, grundy_graph)
        
    #     return game_graph

    @staticmethod
    def create_group_graphs(tab_m):
        group_graphs = []
        for groupe in tab_m:
            config = ConfigurationAllumettes([groupe], 1)
            graph = Graph.create_graph(config)
            group_graphs.append(graph)
        return group_graphs
    
def create_g():
    init = [1, 2, 3]
    ca = ConfigurationAllumettes(init, len(init))

    edges = {}
    edges[ca] = set()
    vertexes = set([Vertex(ca)])

    fc(ca, vertexes, edges)

    g = Graph(vertexes, edges)
    return g


def fc(conf, vertexes, edges):

    if edges.get(conf) == None:
        edges[conf] = set()

    for c in conf.coupsPossibles():
        new = conf.prochaine_configuration(c)
        if not new.estFinale():
            v = Vertex(new)

            vertexes.add(v)

            edges[conf].add(new)
            fc(new, vertexes, edges)



def test_allu():
    g = create_g()

    for v in range(5):
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")

        print(g.grundys_eq(v))

def test_graph():
    init = [1, 2, 3]
    ca = ConfigurationAllumettes(init, len(init))
    # print("Configuration:", ca)

    group_graphs = Graph.create_group_graphs(init)

    # print(group_graphs[0].getEdges())
    # print(group_graphs[1].getEdges())
    # print(group_graphs[2].getEdges())

    print("Valeur de E:", group_graphs[0].E)

    if group_graphs[0].E:
        print("Type de la première clé de E:", type(next(iter(group_graphs[0].E.keys()))))
    else:
        print("Le dictionnaire est vide.")


    print("Valeur de E[Vertex(1)]:", group_graphs[0].E.get(Vertex(1).id))

    print("Valeur de E:", group_graphs[1].E)


    print("Valeur de E[Vertex(2)]:", group_graphs[1].E.get(Vertex(2).id))

    print("Valeur de E[Vertex(2)]:", group_graphs[1].E.get(Vertex(2).id))



    #print(group_graphs[0].E[1])

    #g = Graph.cartesian_sum(group_graphs[0], group_graphs[1])
    #g1 = Graph.cartesian_sum(g, group_graphs[2])




    # print("Configuration:", ca.groupes[0])

    # g1 = Graph.create_graph(ca.groupes[0])
    # g2 = Graph.create_graph(ca.groupes[1])
    # g3 = Graph.create_graph(ca.groupes[2])

    # print("G1:", g1.getEdges())
    # print("G2:", g2.getEdges())
    # print("G3:", g3.getEdges())

test_graph()

