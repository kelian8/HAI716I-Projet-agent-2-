from Strategie import *

class Agent:
    
    strategie : Strategie;
    coupsPerso : list;
    coupsAdv : list;
    score : int;




    def __init__(self, strat,coupsPerso,coupsAdv):
        self.strategie=strat;
        self.coupsPerso = coupsPerso;
        self.coupsAdv=coupsAdv;
        self.score=0;
    
    def jouer(self, jeu):
        return self.strategie.decide(jeu,self.coupsPerso,self.coupsAdv);
