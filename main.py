
from Agent import Agent
from Moteur import Moteur

from strategies.ALLD import ALLD
from strategies.RANDOM import RANDOM
from strategies.TIT_FOR_TAT import TIT_FOR_TAT
from strategies.TESTER import TESTER
from strategies.JOSS import JOSS

#matrice des gains du dilemme du prisonnier
jeu = {
    "C": {
        "C": (3, 3),
        "D": (5, 0)
    },
    "D": {
        "C": (0, 5),
        "D": (2, 2)
    }
}


#Creation des strategies
strategie_ALLD = ALLD()
strategie_RANDOM = RANDOM()
strategie_TIT_FOR_TAT = TIT_FOR_TAT()
strategie_TESTER = TESTER()
strategie_JOSS = JOSS()



#creation des agents
list_agents = []

agent_ALLD = Agent(strategie_ALLD, [], [])
list_agents.append(agent_ALLD)

agent_RANDOM = Agent(strategie_RANDOM, [], [])
list_agents.append(agent_RANDOM)

agent_TIT_FOR_TAT = Agent(strategie_TIT_FOR_TAT, [], [])
list_agents.append(agent_TIT_FOR_TAT)

agent_TESTER = Agent(strategie_TESTER, [], [])
list_agents.append(agent_TESTER)

agent_JOSS = Agent(strategie_JOSS, [], [])
list_agents.append(agent_JOSS)


#deroulement du tournoi chaque agent affronte les autre sur 5 parties de 200 tours
for i in range(len(list_agents)):
    for j in range(i + 1, len(list_agents)):
        agent1=list_agents[i]
        agent2 = list_agents[j]

        if agent1!=agent2:
            moteur = Moteur(agent1 , agent2, jeu)
            for _ in range(0,5):

                agent1.coupsPerso = []
                agent1.coupsAdv = []
                agent2.coupsPerso = []
                agent2.coupsAdv = []
                agent_JOSS.strategie.nb_C = 0 
                                
                moteur.jouer_partie(200)





#Affichage des resultats finaux
print("\n========== RESULTATS ==========")

#tri des agents par score decroissant
agents_tries = sorted(list_agents, key=lambda agent: agent.score, reverse=True)

#affichage
for i, agent in enumerate(agents_tries, start=1):
    print(f"{i}. {agent.strategie.nom} : {agent.score} points")
