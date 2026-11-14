from abc import ABC, abstractmethod

class Strategie(ABC):

    nom : str;

    @abstractmethod
    def decide(self, jeu, coupsPerso, coupsAdv):
        pass

