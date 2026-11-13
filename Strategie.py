from abc import ABC, abstractmethod

class Strategie(ABC):

    nom : string;

    @abstractmethod
    def decide(self, jeu, coupsPerso, coupsAdv):
        pass
     