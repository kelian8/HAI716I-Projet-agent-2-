
from Strategie import *

class TESTER(Strategie):

    def __init__(self):
        self.nom = "TESTER"

    def decide(self, jeu, coupsPerso, coupsAdv):

        #premier tour : on teste l'adversaire
        if len(coupsAdv) == 0:
            return "D"

        #si l'adversaire a riposté au premier tour
        if coupsAdv[0] == "D":

            #on adopter TIT-FOR-TAT
            return coupsAdv[-1]

        #sinon, repeter le cycle C, C, D
        cycle = ["C", "C", "D"]

        return cycle[(len(coupsPerso) - 1) % 3]
