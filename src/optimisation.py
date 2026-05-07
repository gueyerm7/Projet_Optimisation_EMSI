from pulp import *

def resoudre_probleme():

    # Création du problème
    prob = LpProblem("Optimisation_Salles", LpMaximize)

    # Variables
    x1 = LpVariable("Filiere_1", lowBound=0)
    x2 = LpVariable("Filiere_2", lowBound=0)

    # Fonction objectif
    prob += x1 + x2

    # Contraintes
    prob += x1 + 2 * x2 <= 40
    prob += 2 * x1 + x2 <= 50
    prob += x1 + 2 * x2 <= 45

    # Résolution
    prob.solve()

    # Résultats
    resultat = {
        "filiere1": value(x1),
        "filiere2": value(x2),
        "z": value(prob.objective),
        "status": LpStatus[prob.status]
    }

    return resultat