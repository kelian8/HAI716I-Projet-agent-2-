from Strategie import *

class ALLD(Strategie):

    def __init__(self):
        self.nom = "ALL-D"

    def decide(self, jeu, coupsPerso, coupsAdv):
        return "D"