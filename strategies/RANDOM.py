import random
from Strategie import *

class RANDOM(Strategie):

    def __init__(self):
        self.nom = "RANDOM"

    def decide(self, jeu, coupsPerso, coupsAdv):
        return random.choice(["C", "D"])