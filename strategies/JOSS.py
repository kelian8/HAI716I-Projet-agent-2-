import random
from Strategie import *

class JOSS(Strategie):

    def __init__(self):
        self.nom = "JOSS"
        self.nb_C = 0#pour compter le nb de C joués par l'agent 

    def decide(self, jeu, coupsPerso, coupsAdv):

        #premier tour : coopération
        if len(coupsAdv) == 0:
            return "C"

        #comportement TIT-FOR-TAT
        choix = coupsAdv[-1]

        #si on comptait mettre un C et qu'il se trouve ca va etre la 10 eme fois qu'on met un C depuis qu'on a remplace un C par un D alors on remplace par un D
        if choix=="C" and self.nb_C == 9:
            choix = "D"
            self.nb_C = 0
            return choix

        if choix=="C":
            self.nb_C+=1

        return choix