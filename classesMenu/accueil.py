# -*- coding: utf-8 -*-

##################
# accueil du jeu #
##################

#importations
#############
from tkinter import Canvas, Label
from joueur import joueurConnecte
from .classesModifiees import FenetreGrande
from .commandes import Commandes
from .jeu import Jeu
from .joueurs import Joueurs
from .meilleurs import Meilleurs
from .regles import Regles
from constantes import cote_carre

class Accueil(FenetreGrande):
    def __init__(self, **Arguments):
        FenetreGrande.__init__(self, **Arguments)

        self.joueur = joueurConnecte()
        self.peutOuvrir = True
        self.ligneCurseur = 1

        self.canTitre = Canvas(master=self, height=80, width=640)
        self.canTitre.create_text(320, 40, text="TETRIS", font=('Helvetica', 60))
        self.canTitre.grid(row=0, column=0, columnspan=2, pady=10)

        self.canMenu = Canvas(master=self, height=400, width=640)
        self.canMenu.grid(row=1, column=0, columnspan=2)

        self.lignesMenu = {}
        self._construireMenu()
        self._dessinerCurseur()

        self._deplacerCurseur()

        self.bind('<Down>', self.descendreCurseur)
        self.bind('<Up>', self.monterCurseur)
        self.bind('<a>', self.menu)

    def _menus(self):
        joueur = self.joueur
        return [
            f"Jouer ({joueur})",
            "Joueurs",
            "Meilleurs",
            "Commandes",
            "Règles",
            "Quitter"
        ]

    def _construireMenu(self):
        for i, texte in enumerate(self._menus()):
            self.lignesMenu[i] = Label(master=self.canMenu, text=texte, font=('Helvetica', 20), width=20, anchor='w')
            self.lignesMenu[i].grid(row=i, column=1, pady=15, sticky='w')

    def _dessinerCurseur(self):
        c = cote_carre * 2 + 2
        self.curseur = Canvas(master=self.canMenu, height=c, width=c,
                              bg="black", highlightthickness=0)
        self.curseur.create_rectangle(0,          0,          cote_carre, cote_carre, fill="yellow", outline="black")
        self.curseur.create_rectangle(cote_carre, 0,          c - 1,      cote_carre, fill="yellow", outline="black")
        self.curseur.create_rectangle(0,          cote_carre, cote_carre, c - 1,      fill="yellow", outline="black")
        self.curseur.create_rectangle(cote_carre, cote_carre, c - 1,      c - 1,      fill="yellow", outline="black")

    def _deplacerCurseur(self):
        self.curseur.grid(row=self.ligneCurseur - 1, column=0, padx=10)
        self.curseur.update()

    def descendreCurseur(self, event=None):
        self.ligneCurseur = self.ligneCurseur % len(self._menus()) + 1
        self._deplacerCurseur()

    def monterCurseur(self, event=None):
        self.ligneCurseur = (self.ligneCurseur - 2) % len(self._menus()) + 1
        self._deplacerCurseur()

    def majContenu(self):
        """Met à jour le menu après changement de joueur"""
        self.joueur = joueurConnecte()
        for i, texte in enumerate(self._menus()):
            self.lignesMenu[i].config(text=texte)

    def menu(self, event=None):
        if not self.peutOuvrir:
            return
        match self.ligneCurseur - 1:
            case 0:
                self.destroy()
                Jeu().mainloop()
                Accueil().mainloop()
            case 1:
                Joueurs(self)
            case 2:
                Meilleurs(self)
            case 3:
                Commandes(self)
            case 4:
                Regles(self)
            case 5:
                self.destroy()
