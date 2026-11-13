from Agent import *

class Moteur:
    agent1 : Agent;
    agent2 : Agent;
    jeu : list;

    def __init__(self, a1, a2, jeu):
        self.agent1 = a1;
        self.agent2 = a2;
        self.jeu=jeu;

    def jouer_partie(self, n):
        for i in range(0,n):
            print(f"Début partie n°{i}\n");
            print(f"Agent 1 stratégie : {self.agent1.strategie}\n")
            print(f"Agent 2 stratégie : {self.agent2.strategie}\n")

            #les agents décident de leur choix en fonction de leur strategie respective
            choix1 = self.agent1.jouer(self.jeu);
            choix2 = self.agent2.jouer(self.jeu);

            print(f"l'agent 1 a choisi l'option {choix1}\n");
            print(f"l'agent 2 a choisi l'option {choix2}\n");

            #on enregistre les scores respectifs en fonctions des décisions prises par les agents
            score1 = self.jeu[choix2][choix1][0];
            score2 = self.jeu[choix2][choix1][1];

            """
            structure d'un jeu : 
                                          [
                                            j se tait           j avoue            traduction pythons sous forme de dico de dico        [
                                i se tait [  (si,sj)      ,     (si,sj)   ]                          =                                  "D"=["D"=(s1,s2), "C" = (s1,s2)],
                                i avoue   [  (si,sj)      ,     (si,sj)   ]                                                             "C"=["D"=(s1,s2), "C" = (s1,s2)]
                                                                          ]                                                              ]
            """

            print(f"l'agent 1 a remporté {score1} point(s)\n");
            print(f"l'agent 2 a remporté {score2} point(s)\n");

            #mise à jour des score
            self.agent1.score+=score1;
            self.agent2.score+=score2;

            print(f"l'agent 1 a maintenant un score de {self.agent1.score} point(s)\n");
            print(f"l'agent 2 a maintenant un score de {self.agent2.score} point(s)\n");


            #ajouts des coups perso et des adversaire dans la memoire des agents
            self.agent1.coupsPerso.append(choix1);
            self.agent1.coupsAdv.append(choix2);

            self.agent2.coupsPerso.append(choix2);
            self.agent2.coupsAdv.append(choix1);

            print("---------------------------------------------------------\n");
        
        print("Fin de partie!\n")

        if self.agent2.score<self.agent1.score :
            print(f"agent 1 avec strategie {self.agent1.strategie} a gagné!\n");
            return self.agent1.strategie;

        elif self.agent1.score<self.agent2.score :
            print(f"agent 2 avec strategie {self.agent2.strategie} a gagné!\n");
            return self.agent2.strategie;

        else: 
            print("égalité entre les deux stratégies personne ne remporte\n");
            return None;