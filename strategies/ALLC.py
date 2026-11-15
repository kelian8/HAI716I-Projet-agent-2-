from Strategie import *

class ALLC(Strategie):

    def __init__(self):
        self.nom = "ALLC"

    def decide(self, jeu, coupsPerso, coupsAdv):
        return "C"