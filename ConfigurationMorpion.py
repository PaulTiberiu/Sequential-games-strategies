from Configuration import Configuration
from CoupMorpion import CoupMorpion
from copy import deepcopy

class ConfigurationMorpion(Configuration):
    
    def __init__(self):
        super().__init__()
        self.grille = [[None for _ in range(3)] for _ in range(3)]
        
    def __repr__(self) -> str:
        return  '\n'.join([str(i) for i in self.grille])
        
    def __str__(self) -> str:
        return  '\n'.join([str(i) for i in self.grille])


    def prochainJoueur(self):
        if self.historique == [] or self.historique[-1].get_joueur() == 2:
            return 1
        elif self.historique[-1].get_joueur() == 1:
            return 2   
        raise ValueError

    def coupsPossibles(self):
        possibles = []
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == None:
                    possibles.append(CoupMorpion(None, i,j))
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
    

    def f1_geek(self):
        if self.estGagnant(1):
            return 10
        
        elif self.estGagnant(2):
            return -10
        
        else:
            return 0 # Match nul    
        
    def lignesPotentielles(self, C, symbole):
        """
        Renvoie 2 listes des lignes potentielles
        """
        lignes10 = []
        lignes1=[]
        for i in range (3):
            ligne = [C[i][0], C[i][1], C[i][2]]
            if ligne.count(symbole) == 2 and ligne.count(None) == 1:
                lignes10.append(ligne)
            if ligne.count(symbole) == 1 and ligne.count(None) == 2:
                lignes1.append(ligne)
        return lignes10, lignes1
    
    def colonnesPotentielles(self, C, symbole):
        """
        Renvoie 2 listes des colonnes potentielles
        """
        colonnes10 = []
        colonnes1=[]
        for i in range (3):
            colonne = [C[0][i], C[1][i], C[2][i]]
            if colonne.count(symbole) == 2 and colonne.count(None) == 1:
                colonnes10.append(colonne)
            if colonne.count(symbole) == 1 and colonne.count(None) == 2:
                colonnes1.append(colonne)
        return colonnes10, colonnes1
    
    def diagonalesPotentielles(self, C, symbole):
        """
        Renvoie 2 listes des diagonales potentielles
        """
        diagonales10 = []
        diagonales1 = []

        diag_principale = [C[0][0], C[1][1], C[2][2]]
        if diag_principale.count(symbole) == 2 and diag_principale.count(None) == 1:
            diagonales10.append(diag_principale)
        if diag_principale.count(symbole) == 1 and diag_principale.count(None) == 2:
            diagonales1.append(diag_principale)
        
        diag_secondaire = [C[0][2], C[1][1], C[2][0]]
        if diag_secondaire.count(symbole) == 2 and diag_secondaire.count(None) == 1:
            diagonales10.append(diag_secondaire)
        if diag_secondaire.count(symbole) == 1 and diag_secondaire.count(None) == 2:
            diagonales1.append(diag_secondaire)

        return diagonales10, diagonales1
        
    def f1(self):
        score = 0

        if self.estGagnant(1):
            score += 100
            
        # if self.estGagnant(2):
        #     score -= 100

        lignes10, lignes1 = self.lignesPotentielles(self.grille, 1)
        colonnes10, colonnes1 = self.colonnesPotentielles(self.grille, 1)
        diagonales10, diagonales1 = self.diagonalesPotentielles(self.grille, 1)

        # print("lignes10 ", lignes10)
        # print("lignes1 ", lignes1)
        # print("colonnes10 ", colonnes10)
        # print("colonnes1 ", colonnes1)  
        # print("diagonales10 ", diagonales10)    
        # print("diagonales1 ", diagonales1)  
        
        score += len(lignes10) * 10 + len(lignes1)
        score += len(colonnes10) * 10 + len(colonnes1)
        score += len(diagonales10) * 10 + len(diagonales1)

        # print("score ", score)
        return score
    
    # def f1_ntu_line(self, row1, col1, row2, col2,  row3, col3):
    #     score = 0
        
    #     if (self.grille[row1][col1].content == 1) {
    #         score = 1;
    #     } else if (cells[row1][col1].content == 2) {
    #         score = -1;
    #     }
    
    #     if (self.grille[row2][col2].content == 1) {
    #         if (score == 1) {   // cell1 is mySeed
    #             score = 10;
    #         } else if (score == -1) {  // cell1 is 2
    #             return 0;
    #         } else {  // cell1 is empty
    #             score = 1;
    #         }
    #     } else if (self.grille[row2][col2].content == 2) {
    #         if (score == -1) { // cell1 is 2
    #             score = -10;
    #         } else if (score == 1) { // cell1 is 1
    #             return 0;
    #         } else {  // cell1 is empty
    #             score = -1;
    #         }
    #     }
    
    #     if (self.grille[row3][col3].content == mySeed) {
    #         if (score > 0) {  // cell1 and/or cell2 is mySeed
    #             score *= 10
    #         } else if (score < 0) {  // cell1 and/or cell2 is oppSeed
    #             return 0
    #         } else {  // cell1 and cell2 are empty
    #             score = 1
    #         }
    #     } else if (self.grille[row3][col3].content == oppSeed) {
    #         if (score < 0) {  // cell1 and/or cell2 is oppSeed
    #             score *= 10;
    #         } else if (score > 1) {  // cell1 and/or cell2 is mySeed
    #             return 0
    #         } else {  // cell1 and cell2 are empty
    #             score = -1
    #         }
    #     }
    #     return score

    # def f1_ntu(self):
    #    return 

      
        