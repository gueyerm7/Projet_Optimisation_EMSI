import customtkinter as ctk
from pulp import *
import matplotlib.pyplot as plt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Optimisation EMSI Marrakech")
        self.geometry("700x600")

        # Titre
        titre = ctk.CTkLabel(
            self,
            text="OPTIMISATION EMSI MARRAKECH",
            font=("Arial", 24, "bold")
        )
        titre.pack(pady=20)

        # Frame principal
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Contraintes

        self.label1 = ctk.CTkLabel(frame, text="Capacité Salles")
        self.label1.pack(pady=5)

        self.entree1 = ctk.CTkEntry(frame)
        self.entree1.insert(0, "40")
        self.entree1.pack(pady=5)

        self.label2 = ctk.CTkLabel(frame, text="Capacité Enseignants")
        self.label2.pack(pady=5)

        self.entree2 = ctk.CTkEntry(frame)
        self.entree2.insert(0, "50")
        self.entree2.pack(pady=5)

        self.label3 = ctk.CTkLabel(frame, text="Emploi du Temps")
        self.label3.pack(pady=5)

        self.entree3 = ctk.CTkEntry(frame)
        self.entree3.insert(0, "45")
        self.entree3.pack(pady=5)

        # Bouton
        bouton = ctk.CTkButton(
            frame,
            text="Résoudre le problème",
            command=self.resoudre
        )
        bouton.pack(pady=20)

        # Zone résultats
        self.resultats = ctk.CTkTextbox(
            frame,
            width=500,
            height=200
        )
        self.resultats.pack(pady=10)

    def resoudre(self):

        salles = float(self.entree1.get())
        enseignants = float(self.entree2.get())
        emploi = float(self.entree3.get())

        # Modèle
        prob = LpProblem("Optimisation", LpMaximize)

        x1 = LpVariable("Filiere_1", lowBound=0)
        x2 = LpVariable("Filiere_2", lowBound=0)

        # Fonction objectif
        prob += x1 + x2

        # Contraintes
        prob += x1 + 2 * x2 <= salles
        prob += 2 * x1 + x2 <= enseignants
        prob += x1 + 2 * x2 <= emploi

        # Résolution
        prob.solve()

        f1 = value(x1)
        f2 = value(x2)
        z = value(prob.objective)

        # Affichage résultats
        self.resultats.delete("1.0", "end")

        texte = f"""
========= RESULTATS =========

Status : {LpStatus[prob.status]}

Filière 1 : {f1} heures
Filière 2 : {f2} heures

Valeur optimale Z : {z}
"""

        self.resultats.insert("end", texte)

        # Graphique
        filieres = ["Filière 1", "Filière 2"]
        heures = [f1, f2]

        plt.figure(figsize=(6, 4))
        plt.bar(filieres, heures)

        plt.title("Répartition optimale")
        plt.ylabel("Heures")

        plt.show()


app = Application()
app.mainloop()