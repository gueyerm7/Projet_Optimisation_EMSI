import matplotlib.pyplot as plt

def afficher_graphique(f1, f2):

    filieres = ["Filière 1", "Filière 2"]
    heures = [f1, f2]

    plt.figure(figsize=(8, 5))

    barres = plt.bar(filieres, heures)

    plt.title("Répartition optimale des heures")
    plt.ylabel("Nombre d'heures")

    # Afficher les valeurs sur les barres
    for barre in barres:
        hauteur = barre.get_height()

        plt.text(
            barre.get_x() + barre.get_width() / 2,
            hauteur,
            f'{hauteur}',
            ha='center',
            va='bottom'
        )

    plt.tight_layout()

    plt.savefig("../images/graphique.png")

    plt.show()