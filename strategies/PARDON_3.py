from Strategie import *

class PARDON_3(Strategie):

    def __init__(self):
        self.nom = "PARDON_3"
        self.nb_punitions = 0

    def decide(self, jeu, coupsPerso, coupsAdv):

        # Premier tour : coopération
        if len(coupsAdv) == 0:
            return "C"

        #si ona toujours pas pardonné on continue a jouer D (on pardonne au bout de 3 D)
        if self.nb_punitions > 0:
            self.nb_punitions -= 1
            return "D"

        #si l'adversaire vient de trahir
        if coupsAdv[-1] == "D":
            self.nb_punitions = 2
            return "D"

        #sinon on coopere 
        return "C"
