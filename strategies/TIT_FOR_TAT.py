
from Strategie import *

class TIT_FOR_TAT(Strategie):

    def __init__(self):
        self.nom = "TIT-FOR-TAT"

    def decide(self, jeu, coupsPerso, coupsAdv):

        # Premier tour : cooperation
        if len(coupsAdv) == 0:
            return "C"

        #tours suivants : reproduire le dernier coup adverse
        return coupsAdv[-1]
