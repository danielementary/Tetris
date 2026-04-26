# -*- coding: utf-8 -*-

###################
#Commandes du jeu #
###################

#importations
#############
from tkinter import Label
from .classesModifiees import FenetrePetite

#commandes
##########

texteCommandes = [
    ("D-pad gauche/droite", "Déplacer la pièce"),
    ("D-pad bas",           "Accélérer la chute"),
    ("A",                   "Tourner dans le sens horaire"),
    ("B",                   "Tourner dans le sens anti-horaire"),
    ("Start",               "Mettre le jeu en pause"),
    ("Select",              "Changer de thème"),
]

class Commandes(FenetrePetite):
    def __init__(self, parent, **Arguments):
        FenetrePetite.__init__(self, parent, "COMMANDES", **Arguments)
        for commande, description in texteCommandes:
            Label(self, text=f"{commande} : {description}", wraplength=400, font=('Helvetica', 15)).pack(pady=5)
