from Vertex import Vertex

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
