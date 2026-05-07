# -*- coding: utf-8 -*-
from optimisation import resoudre_probleme
from graphique import afficher_graphique
from datetime import datetime

# Titre
print("=" * 45)
print("   OPTIMISATION EMSI MARRAKECH")
print("=" * 45)

print("\nRésolution du problème en cours...\n")

# Résolution
resultat = resoudre_probleme()

# Affichage console
print("=" * 45)
print("            RESULTATS")
print("=" * 45)

print(f"\nStatus : {resultat['status']}")

print(f"\nFilière 1 : {resultat['filiere1']} heures")
print(f"Filière 2 : {resultat['filiere2']} heures")

print(f"\nValeur optimale Z : {resultat['z']}")

print("\nGraphique généré avec succès.")
print("Fichier résultat sauvegardé.")

# Sauvegarde fichier texte
with open("../resultats/resultat.txt", "w", encoding="utf-8") as fichier:

    fichier.write("===== RESULTATS =====\n\n")

    fichier.write(f"Date : {datetime.now()}\n\n")

    fichier.write(f"Status : {resultat['status']}\n")
    fichier.write(f"Filière 1 : {resultat['filiere1']} heures\n")
    fichier.write(f"Filière 2 : {resultat['filiere2']} heures\n")
    fichier.write(f"Valeur optimale Z : {resultat['z']}\n")

# Affichage graphique
afficher_graphique(
    resultat["filiere1"],
    resultat["filiere2"]
)

print("\nProgramme terminé avec succès.")