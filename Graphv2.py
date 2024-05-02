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

    def __repr__(self) -> str:
        return str([v for v in self.V])


    def grundys(self):
        return '\n'.join([ str(v) for v in self.V])
    
    def grundys_eq(self, val):
        return '\n'.join([ str(v) for v in self.V if v.grundy == val])
    
    def insert_edge(self, v1, v2): 
        """
        Permet d'ajouter une arrete
        """

        self.E[v1].add(v2)

    def insert_vertex(self, v):
        self.V.add(v)

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

def cartesian_sum(G1, G2):
    X = set()
    for vertex1 in G1.V:
        for vertex2 in G2.V:
            new_vertex_id = vertex1.id + "-" + vertex2.id
            X.add(Vertex(new_vertex_id))

    L = dict()
    for vertex1 in G1.V:
        for vertex2 in G2.V:
            key = vertex1.id + "-" + vertex2.id
            L[key] = set()

    for vertex in X:
        vertex1_id, vertex2_id = vertex.id.split("-")
        print("Vertex1:", vertex1_id, " Vertex2:", vertex2_id)

        for child1 in G1.E[vertex1_id]:
            print("Child1:", child1)
            L[vertex.id].add(child1 + "-" + vertex2_id)

        for child2 in G2.E[vertex2_id]:
            print("Child2:", child2)
            L[vertex.id].add(vertex1_id + "-" + child2)
        
    G = Graph(X, L)
    return G




    
def test_cartesian_sum():
    G1 = Graph({Vertex("x1"), Vertex("y1"), Vertex("z1")})
    G1.insert_edge("x1", "y1")
    G1.insert_edge("x1", "z1")
    G1.compute_all_grundys()
    print("Ensemble de sommets X pour G:", G1.V)
    print("Ensemble d'arêtes L pour G:", G1.E)


    G2 = Graph({Vertex("x2"), Vertex("t2")})
    G2.insert_edge("x2", "t2")
    G2.compute_all_grundys()
    print("Ensemble de sommets X pour G:", G2.V)
    print("Ensemble d'arêtes L pour G:", G2.E)

    G = cartesian_sum(G1, G2)
    G.compute_all_grundys()
    print("Ensemble de sommets X pour G:", G.V)
    print("Ensemble d'arêtes L pour G:", G.E)

test_cartesian_sum()

    


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



def create_g():
    init = [1, 3, 5]
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
    g.compute_all_grundys()


    for v in range(5):
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")

        print(g.grundys_eq(v))

test_allu()