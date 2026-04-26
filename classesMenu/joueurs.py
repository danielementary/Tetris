# -*- coding: utf-8 -*-

#################
#Choix du joueur#
#################

#importations
#############
from tkinter import Label
from .classesModifiees import FenetrePetite
from constantes import listeJoueurs
from joueur import joueurConnecte, connexion

class Joueurs(FenetrePetite):
    def __init__(self, parent, **Arguments):
        FenetrePetite.__init__(self, parent, "JOUEURS", **Arguments)

        self.joueur_actif = joueurConnecte()
        self.index = listeJoueurs.index(self.joueur_actif) if self.joueur_actif in listeJoueurs else -1

        self.label = Label(self, font=('Helvetica', 20))
        self.label.pack(pady=20)

        Label(self, text="↑ ↓ pour naviguer  •  A pour sélectionner",
              font=('Helvetica', 15)).pack(pady=5)

        self.majAffichage()

        self.bind('<Up>', self.precedent)
        self.bind('<Down>', self.suivant)
        self.bind('<a>', self.selectionner)

    def majAffichage(self):
        joueur = listeJoueurs[self.index]
        est_actif = joueur == self.joueur_actif
        texte = f"→ {joueur} ←" if est_actif else joueur
        self.label.config(text=texte, font=('Helvetica', 20, 'bold' if est_actif else ''))

    def precedent(self, event=None):
        self.index = (self.index - 1) % len(listeJoueurs)
        self.majAffichage()

    def suivant(self, event=None):
        self.index = (self.index + 1) % len(listeJoueurs)
        self.majAffichage()

    def selectionner(self, event=None):
        connexion(listeJoueurs[self.index])
        self.joueur_actif = listeJoueurs[self.index]
        self.parent.majContenu()
        self.quitter()
