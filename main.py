
from Agent import Agent
from Moteur import Moteur

from strategies.ALLD import ALLD
from strategies.RANDOM import RANDOM


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


#creation des agents
list_agents = []

agent_ALLD = Agent(strategie_ALLD, [], [])
list_agents.append(agent_ALLD)

agent_RANDOM = Agent(strategie_RANDOM, [], [])
list_agents.append(agent_RANDOM)



#deroulement du tournoi chaque agent affronte les autre sur 5 parties de 200 tours
for agent1 in list_agents:
    for agent2 in list_agents:
        if agent1!=agent2:
            moteur = Moteur(agent1 , agent2, jeu)
            for _ in range(0,5):
                moteur.jouer_partie(200)





#Affichage des resultats finaux
print("\n========== RESULTATS ==========")

#tri des agents par score decroissant
agents_tries = sorted(list_agents, key=lambda agent: agent.score, reverse=True)

#affichage
for i, agent in enumerate(agents_tries, start=1):
    print(f"{i}. {agent.strategie.nom} : {agent.score} points")
