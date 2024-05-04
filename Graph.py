import itertools
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
            if type(next(iter(V))) == Vertex:
                self.E = {i.id : set() for i in V}
            else :
                if type(next(iter(V))) == tuple:
                    self.E = {((j.id) for j in i) : set() for i in V} # Creer le dictionnaire qui relie le sommet i a vide
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
    def create_graph(configuration, zeros = False):

        edges = {}
        edges[configuration] = set()
        vertexes = set([Vertex(configuration)])

        Graph.complete_graph(configuration, vertexes, edges, zeros)
        g = Graph(vertexes, edges)

        g.compute_all_grundys()
        return g

    
    @staticmethod
    def complete_graph(conf, vertexes, edges, zeros = False):

        if edges.get(conf) == None:
            edges[conf] = set()

        for c in conf.coupsPossibles():
            new = conf.prochaine_configuration(c)
            if zeros:
                v = Vertex(new)

                vertexes.add(v)

                
                edges[conf].add(new)
                Graph.complete_graph(new, vertexes, edges, zeros)
            
            else :
                if not new.estFinale():
                    v = Vertex(new)

                    vertexes.add(v)

                    
                    edges[conf].add(new)
                    Graph.complete_graph(new, vertexes, edges, zeros)


    @staticmethod
    def cartesian_sum(first ,second):
        vertexes = set()
        edges = {}
        
        hasTuples = False

        for vertex1 in first.V:
            for vertex2 in second.V:
                if type(vertex1) == tuple:
                    new_vertex = (*vertex1, vertex2)
                    hasTuples = True  
                else:
                    new_vertex = (vertex1, vertex2)
                vertexes.add(new_vertex)
        

        for v in vertexes:
            edges[v] = set()

        for v in vertexes:
            if hasTuples:  
                firstSource = v[:-1]

                secondSource = v[-1].id
                
                for desc in first.E[firstSource]:
                    new_desc = (*desc, secondSource)
                    edges[v].add( new_desc )

                for desc in second.E[secondSource]:
                    new_desc = (*firstSource, desc)
                    edges[v].add( new_desc )

  
            else:
                firstSource = v[0].id   
                secondSource = v[1].id

                for desc in first.E[firstSource]:
                    new_desc = (desc, secondSource)
                    edges[v].add( new_desc )

                for desc in second.E[secondSource]:
                    new_desc = (firstSource, desc)
                    edges[v].add( new_desc )

        return Graph(vertexes, edges)


    @staticmethod
    def digital_sum(numbers):
        # Convertir chaque nombre en binaire et les stocker dans une liste
        binary_numbers = [bin(num)[2:].zfill(len(bin(max(numbers)))) for num in numbers]

        # Obtenir la longueur maximale des nombres binaires
        max_length = len(max(binary_numbers, key=len))

        # Ajuster la longueur de chaque nombre binaire pour qu'ils aient la même longueur
        binary_numbers = [binary.ljust(max_length, '0') for binary in binary_numbers]

        # Calculer la somme digitale
        result = 0
        for binary in binary_numbers:
            result ^= int(binary, 2)

        return result
    
    def all_digital_sums(self):
        ret = []
        for vertex in self.V:
            if type(vertex) == tuple:
                maped = map(lambda v : v.grundy, vertex)
                ret.append(   Graph.digital_sum(list(maped)) )
            else :
                ret.append(vertex.grundy)

        return ret
    
    @staticmethod
    def digital_sum_of(vertexes):
        if type(vertexes) == tuple:
            maped = map(lambda v : v.grundy, vertexes)
            return  Graph.digital_sum(list(maped))
        else :
            return vertexes.grundy


    @staticmethod
    def final_graph(product):
        
        vertexes = set()
        edges = {}
        for v in product.V:
            nv = Vertex(v)
            vertexes.add(nv)
            nv.setGrundy(Graph.digital_sum_of(v))
            edges[v] = set()

            for ed in product.E[v]:
                edges[v].add(ed)

        return Graph(vertexes, edges)
        



        
    @staticmethod
    def create_group_graphs(tab_m):
        group_graphs = []
        for groupe in tab_m:
            config = ConfigurationAllumettes([groupe], 1)
            graph = Graph.create_graph(config, zeros = True)
            group_graphs.append(graph)
        return group_graphs
    

    def getGrundyMulti(self, config):

        for vertex in self.V:

            mapped = map(lambda vert : vert.id.groupes[0], vertex.id)
            consum = list(mapped)
            
    
            conf = ConfigurationAllumettes(consum, len(consum))
                        
            if config == conf:
                return vertex.grundy
        
        raise ValueError("iiiiii")



    
def test_allumettes():
    tab_m = [1, 2, 1]
    group_graphs = Graph.create_group_graphs(tab_m)

    # print("Group Graphs")
    # for g in group_graphs:
    #     print(g.getEdges())
    #     print("")

    product = group_graphs[0]

    for i in range(1, len(group_graphs)):
        product = Graph.cartesian_sum(product, group_graphs[i])
    
    final = Graph.final_graph(product)
    print(final.E)

    print("")
    #print(final.grundys())

#test_allumettes()

