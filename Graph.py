from Vertex import Vertex
from ConfigurationAllumettes import ConfigurationAllumettes
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

    def __repr__(self) -> str:
        return str([v for v in self.V])

    def insert_edge(self, v1, v2): 
        """
        Permet d'ajouter une arrete
        """

        self.E[v1].add(v2)

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
        
        while True :
            for child in self.E[vertex.id]:
                if self.getVertex(child).grundy == grundy:
                    grundy = grundy + 1
            break
        vertex.setGrundy(grundy)


def test_graph():
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    h = Vertex("H")
    i = Vertex("I")
    j = Vertex("J")
    k = Vertex("K")
    l = Vertex("L")
    
    li = [a, b, c, d, e, f, g, h ,i, j ,k ,l]
    verts = set()
    
    for v in li:
        verts.add(v)

    g = Graph(verts)

    g.insert_edge("A", "B")
    g.insert_edge("A", "C")
    g.insert_edge("A", "D")
    g.insert_edge("A", "E")

    g.insert_edge("B", "F")

    g.insert_edge("C", "H")

    g.insert_edge("D", "G")

    g.insert_edge("E", "J")
    g.insert_edge("E", "K")


    g.insert_edge("F", "I")

    g.insert_edge("G", "H")


    g.insert_edge("I", "L")
    g.insert_edge("H", "L")
    g.insert_edge("J", "L")

    g.compute_all_grundys()
    for i in g.V:
        print(i)



def test_allu():
    t = [3, 4, 5]
    ca = ConfigurationAllumettes(t, len(t))
    print(ca)

test_allu()