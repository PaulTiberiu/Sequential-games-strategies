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