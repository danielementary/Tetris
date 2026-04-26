# -*- coding: utf-8 -*-

##########################
#Meilleurs scores du jeu #
##########################

#importations
#############
from tkinter import Label
from .classesModifiees import FenetrePetite
from sgbd import recupererScores
from joueur import joueurConnecte

class Meilleurs(FenetrePetite):
    def __init__(self, parent, **Arguments):
        FenetrePetite.__init__(self, parent, "MEILLEURS", **Arguments)

        Label(self, text=f"{'Rang':<6}{'Joueur':<12}{'Score':<10}{'Lignes'}",
              font=('Courier', 12, 'bold')).pack(pady=5)

        joueur_actif = joueurConnecte()
        scores = recupererScores()

        if not scores:
            Label(self, text="Aucun score enregistré.",
                  font=('Helvetica', 12)).pack(pady=10)
            return

        for rang, (joueurScore, points, lignes) in enumerate(scores, start=1):
            est_connecte = joueur_actif == joueurScore
            poids = 'bold' if est_connecte else ''
            Label(self,
                  text=f"{rang:<6}{joueurScore:<12}{points:<10}{lignes}",
                  font=('Courier', 12, poids)).pack(pady=3)
