############################################
# Q1.1
############################################

from copy import deepcopy
import random
from time import perf_counter as pc



class JeuSequentiel:
    """Represente un jeu sequentiel, a somme
    nulle, a information parfaite"""
    def __init__(self):
        pass

    def joueurCourant(self, C):
        """Rend le joueur courant dans la
        configuration C"""
        raise NotImplementedError

    def coupsPossibles(self, C):
        """Rend la liste des coups possibles dans
        la configuration C"""
        return C.coupsPossibles()

    def f1(self, C):
        """Rend la valeur de l'evaluation de la configuration C pour le joueur 1"""
        raise NotImplementedError

    def joueLeCoup(self, C, coup):
        """Rend la configuration obtenue apres que le joueur courant ait joue le coup
        dans la configuration C"""
        raise NotImplementedError

    def estFini(self, C):
        """ Rend True si la configuration C est
        une configuration finale"""
        return C.estFinale()

    def prochaine_configuration(self, C, coup):
        raise NotImplementedError
    

############################################
# Q1.2
############################################
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
        return C.estFinale()
    
    def estGagnant(self, C,  joueur):
        """
        Verifie si le joueur donné a gagne dans la configuration actuelle.
        """
        return C.estGagnant(joueur)

    def jouerPartie(self, C, strategie, *args):
        st = strategie.__new__(strategie)
        st.__init__(self, *args)

        #print("debut")

        while not(self.estFinale(C)):
           
            coup = st.choisirProchainCoup(C)

            #print("Coup : ", coup)
            self.joueLeCoup(C, coup)
            #print(C)

            if self.estFinale(C) : break
        
            coup = st.choisirProchainCoup(C)
            self.joueLeCoup(C, coup)

            #print("Coup : ", coup)
        
        print(C)

        if self.estGagnant(C, 1):
            return 1
        elif self.estGagnant(C, 2):
            return 2
        else:
            return None


class Coup:
    def __init__(self, joueur):
        self.joueur = joueur

    def get_joueur(self):
        return self.joueur

    def position(self):
        raise NotImplementedError
    
class Configuration:
    
    def __init__(self):
        self.historique = []

    def getDernierCoup(self):
        return self.historique[-1]

    def prochainJoueur(self):
        pass

    def coupsPossibles(self):
        pass

    def estFinale(self):
        pass

class CoupMorpion(Coup):
    def __init__(self, joueur, x, y):
        super().__init__(joueur)
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def position(self):
        return self.get_x(), self.get_y()
    
    def __repr__(self):
        return f"joueur {self.get_joueur()} : ({self.get_x()},{self.get_y()})"

class ConfigurationMorpion(Configuration):
    
    def __init__(self):
        super().__init__()
        self.grille = [[None for _ in range(3)] for _ in range(3)]
        
    def __repr__(self) -> str:
        return '\n'.join([str(i) for i in self.grille]) + '\n'
        
    def __str__(self) -> str:
        return '\n'.join([str(i) for i in self.grille]) + '\n'


    def prochainJoueur(self):
        if self.historique == [] or self.getDernierCoup().get_joueur() == 2:
            return 1
        elif self.getDernierCoup().get_joueur() == 1:
            return 2   
        raise ValueError

    def coupsPossibles(self):
        possibles = []
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == None:
                    possibles.append(CoupMorpion(self.prochainJoueur(), i,j))
        return possibles

    def estFinale(self):
        return self.estGagnant(1) or self.estGagnant(2) or self.coupsPossibles() == []
    
    def estGagnant(self, joueur):
        # Verifier les lignes
        for i in range(3):
            if all(cell == joueur for cell in self.grille[i]):
                return True
        
        # Verifier les colonnes
        for j in range(3):
            if all(self.grille[i][j] == joueur for i in range(3)):
                return True
            
        # Verifier les diagonales
        if all(self.grille[i][i] == joueur for i in range(3)) or all(self.grille[i][2 - i] == joueur for i in range(3)):
            return True

        return False
    
    def jouer_coup(self, coup):
        """joue le coup"""
        x, y = coup.position()
        self.grille[x][y] = coup.get_joueur()
        self.historique.append(coup)

    def prochaine_configuration(self, coup):
        """renvoie la prochaine configuration si le coup est joué"""
        
        cp = deepcopy(self)
        cp.jouer_coup(coup)
        return cp
    

    def f1(self):
        if self.estGagnant(1):
            return 1
        
        elif self.estGagnant(2):
            return -1
        
        else:
            return 0 # Match nul
        
        
############################################
# Q2.1
############################################

class Strategie():
    """
    Represente une strategie de jeu
    """

    def __init__(self, jeu: JeuSequentiel):
        self.jeu = jeu

    def choisirProchainCoup(self, C):
        """
        Choisit un coup parmi les coups possibles dans la configuration C
        """
        raise NotImplementedError
    
############################################
# Q2.2
############################################

class StrategieAleatoire(Strategie):    
    """
    Represente une strategie de jeu aleatoire pour tout jeu sequentiel
    """
    def __init__(self, jeu: JeuSequentiel):
        super().__init__(jeu)

    def choisirProchainCoup(self, C):
        """
        Choisit un coup aleatoire suivant une distribution uniforme sur tous les coups possibles
        dans la configuration C
        """
        return random.choice(C.coupsPossibles())
    

############################################
# Q2.3
############################################

def Alea_Morpion():
    jeu = Morpion()
    C = ConfigurationMorpion()
    gagnant = jeu.jouerPartie(C, StrategieAleatoire)
    return gagnant

############################################
# Q3.1
############################################

class StrategieMinMax(Strategie):
    """
    Represente une strategie utilisant un arbre min-max de profondeur k
    """

    def __init__(self, jeu: JeuSequentiel, k: int):
        super().__init__(jeu)
        self.profondeur_max = k

    def minimax(self, C, profondeur, maximise):
        coupsPossibles = self.jeu.coupsPossibles(C)
        meilleur_coup = None


        if profondeur == 0 or self.jeu.estFini(C):
            return C.f1(), None, profondeur


        if maximise:
            meilleur_score = float("-inf")
            meilleur_profondeur = 0

            for coup in coupsPossibles:
                config_suivante = self.jeu.prochaine_configuration(C, coup)
                m_score, m_coup, m_profondeur = self.minimax(config_suivante, profondeur - 1, False)
                # meilleur_score = max(meilleur_score, m_score)
                # if meilleur_score == m_score:
                #     meilleur_coup = coup
                if meilleur_score == m_score:
                    meilleur_profondeur = max(meilleur_profondeur, m_profondeur)
                    if meilleur_profondeur == m_profondeur:
                        meilleur_coup = coup
                        meilleur_score = m_score
                else :
                    meilleur_score = max(meilleur_score, m_score)
                    if meilleur_score == m_score:
                        meilleur_coup = coup
                        meilleur_profondeur = m_profondeur


            return meilleur_score, meilleur_coup, meilleur_profondeur

        else:
            meilleur_score = float("inf")
            meilleur_profondeur = 0

            for coup in coupsPossibles:
                config_suivante = self.jeu.prochaine_configuration(C, coup)
                m_score, m_coup, m_profondeur = self.minimax(config_suivante, profondeur - 1, True)
                if meilleur_score == m_score:
                    meilleur_profondeur = max(meilleur_profondeur, m_profondeur)
                    if meilleur_profondeur == m_profondeur:
                        meilleur_coup = coup
                        meilleur_score = m_score
                else :
                    meilleur_score = min(meilleur_score, m_score)
                    if meilleur_score == m_score:
                        meilleur_coup = coup
                        meilleur_profondeur = m_profondeur

            return meilleur_score, meilleur_coup, meilleur_profondeur


    def choisirProchainCoup(self, C):
        #coup = self.prepare_negamax(C)
        maximise = self.jeu.joueurCourant(C) == 1
        _, coup, _ = self.minimax(C, 9, maximise)
        return coup

############################################
# Q4.1
############################################

class Allumettes(JeuSequentiel):
    """
    Represente le jeu des allumettes avec g groupes de m allumettes chacun.
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
        return C.f1()

    def joueLeCoup(self, C, coup):
        """
        Renvoie la configuration obtenue apres que le joueur courant ait joue le coup dans la configuration C.
        """
        return C.joueLeCoup(coup)
    
    def estFinale(self, C):
        return C.estFinale()    

    def joueurCourant(self, C):
        """"
        Rend le joueur courant dans la configuration C
        """
        return C.prochainJoueur()
    
    def prochaine_configuration(self, C, coup):
        return C.prochaine_configuration(coup)
    
    def estGagnant(self, C):
        return C.estGagnant()


    def jouerPartie(self, C, strategie, *args):
        st = strategie.__new__(strategie)
        st.__init__(self, *args)

       # print("debut")
        
        while not(self.estFinale(C)):
           
            coup = st.choisirProchainCoup(C)

            # print("Coup : ", coup)
            self.joueLeCoup(C, coup)
            # print(C)

            if self.estFinale(C) : break
        
            coup = st.choisirProchainCoup(C)
            self.joueLeCoup(C, coup)

            # print("Coup : ", coup)
            # print(C)

        return 1 if self.estGagnant(C) else 2

class CoupAllumettes(Coup):
    def __init__(self, joueur, count, row):
        super().__init__(joueur)
        self.count = count
        self.row = row

    def get_row(self):
        return self.row
    
    def get_count(self):
        return self.count
    
    def position(self):
        return self.get_row()
    
    def __repr__(self):
        return f"joueur {self.get_joueur()} : row {self.position()}, count = {self.get_count()}"

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

    def coupsPossibles(self):
        """
        Renvoie la liste des coups possibles dans la configuration C
        """
        coups = []
        for i, groupe in enumerate(self.groupes):
            if groupe > 0:
                # Pour chaque groupe restant, les coups possibles sont de retirer 1 a groupe jusqu'a 0
                for j in range(1, groupe + 1):
                    coups.append(CoupAllumettes(self.prochainJoueur(), j, i)) # (indice du groupe, nb d'allumettes a retirer)

        return coups

    def f1(self):
        if self.estFinale():
           return 1 if (self.getDernierCoup().get_joueur() != 1) else -1
        return 0
 

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
    
    def estGagnant(self):
        return self.getDernierCoup().get_joueur() == 2
      

    def estFinale(self):
        return all(groupe == 0 for groupe in self.groupes)
    
class Vertex:
    def __init__(self, id):
        self.id = id
        self.grundy = None

    def setGrundy(self, value):
        self.grundy = value

    def __str__(self) -> str:
        return "Sommet " + str(self.id) + " grundy = " + str(self.grundy)
    
    def __repr__(self) -> str:
        return "Sommet " + str(self.id) + " grundy = " + str(self.grundy)
    
    def __eq__(self, other) -> bool:
        return self.id == other.id
    
    def __lt__(self, other):
        return self.id < other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
    

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
        
        return random.choice(coups)
    
    def precompute_graph(self, C):
        return Graph.create_graph(C)
    

class StrategieGrundyOpti(Strategie):


    def __init__(self, jeu: JeuSequentiel):
        self.jeu = jeu

    def choisirProchainCoup(self, C):
        coups = []
        zeros= []
        graph = self.compute_graph(C)

        for coup in C.coupsPossibles():
            config = C.prochaine_configuration(coup)

            if not config.estFinale():
                
                grundy = graph.getGrundyMulti(config)
                #print(coup, " grundy coup = ", grundy)
                if grundy == 0:
                    zeros.append(coup)
        
            coups.append(coup)
        
        if zeros:
            return random.choice(zeros)
        return random.choice(coups)
    
    def compute_graph(self, C):
        tab_m = C.groupes
        group_graphs = Graph.create_group_graphs(tab_m)

        product = group_graphs[0]

        for i in range(1, len(group_graphs)):
            product = Graph.cartesian_sum(product, group_graphs[i])
        
        final = Graph.final_graph(product)

        return final


############################################
# Q5
############################################

def MinMax_Morpion(profondeur):
    partie = Morpion()

    cg = ConfigurationMorpion()
    
    gagnant = partie.jouerPartie(cg, StrategieMinMax, profondeur)

    return gagnant

def random_Allu(groupes, len_groupes):
    partie = Allumettes()
    cg = ConfigurationAllumettes(groupes, len_groupes)
    gagnant = partie.jouerPartie(cg, StrategieAleatoire)
    return gagnant

def MinMax_Allu(groupes, len_groupes, profondeur):
    partie = Allumettes()
    cg = ConfigurationAllumettes(groupes, len_groupes)
    gagnant = partie.jouerPartie(cg, StrategieMinMax, profondeur)
    return gagnant

def Grundy_Allu(groupes, len_groupes):
    partie = Allumettes()
    cg = ConfigurationAllumettes(groupes, len_groupes)
    gagnant = partie.jouerPartie(cg, StrategieGrundy, cg)
    return gagnant


def comparaison_methodes_Allu(loops, cols, maxallu, profondeur):
    
    
    partie = Allumettes()
    times = {}


    for _ in range(loops):
        groupes = []

        for _ in range(cols):
            groupes.append(random.randint(1, maxallu))

        
        cg = ConfigurationAllumettes(groupes, len(groupes))
        
        strats = [StrategieAleatoire, StrategieMinMax, StrategieGrundy, StrategieGrundyOpti]
        copies = [deepcopy(cg) for _ in strats]
        args = [None, profondeur, copies[2], None]
        
        times[cg] = {}
        
        print("conf  ", cg)


        for idx, strat in enumerate(strats):
            times[cg][strat] = {}
            # print("debut ", strat)

            now = pc()

            if args[idx]:
                g = partie.jouerPartie(copies[idx], strat, args[idx])
            else:
                g = partie.jouerPartie(copies[idx], strat)
            
            
            later = pc()
            
            #print(times[cg])
            times[cg][strat]["temps"] = later - now
            times[cg][strat]["gagnant"] = g
 
    return times






