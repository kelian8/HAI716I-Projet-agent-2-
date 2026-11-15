from Strategie import *

class ALLD(Strategie):

    def __init__(self):
        self.nom = "ALLD"

    def decide(self, jeu, coupsPerso, coupsAdv):
        return "D"