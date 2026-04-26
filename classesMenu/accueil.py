# -*- coding: utf-8 -*-

##################
# accueil du jeu #
##################

#importations
#############
from joueur import joueurConnecte

from tkinter import *
from tkinter.messagebox import *

from .classesModifiees import *
from .commandes import *
from .jeu import *
from .meilleursScores import *
from .regles import *

from constantes import *

class Accueil(FenetreGrande):
    def __init__(self, **Arguments):
        FenetreGrande.__init__(self, **Arguments)

        self.lignesMenu = {}
        self.joueur = joueurConnecte()

        self.canTitre = Canvas(master=self, height=80, width=640)
        self.canTitre.create_text(320, 40, text="TETRIS", font=('Helvetica', 60))
        self.canTitre.grid(row=1,column=0, columnspan=2, pady=10)

        self.canMenu = Canvas(master=self, height=480-80, width=640)
        self.canMenu.grid(row=2, column=1)

        for i in range(self.nombreMenus()):
            self.lignesMenu[i] = Label(master=self.canMenu, text=self.menus()[i], font=('Helvetica', 20))
            self.lignesMenu[i].grid(row=i+1, column=1, pady=15, sticky=W)

        self.ligneCurseur = 1

        self.curseur = Canvas(master=self.canMenu, height=52, width=52)
        self.curseur.grid(row=self.ligneCurseur, column=0, padx=50)

        self.curseur.create_rectangle(2, 2, 27, 27, fill="yellow")
        self.curseur.create_rectangle(2, 27, 27, 52, fill="yellow")
        self.curseur.create_rectangle(27, 2, 52, 27, fill="yellow")
        self.curseur.create_rectangle(27, 27, 52, 52, fill="yellow")

        self.peutOuvrir = True

        self.bind('<Down>', self.descendreCurseur)
        self.bind('<Up>', self.monterCurseur)
        self.bind('<a>', self.menu)

    def menus(self):
        return [
            f"Jouer ({self.joueur})",
            "Joueurs",
            "Meilleurs",
            "Commandes",
            "Règles",
            "Quitter"
        ]

    def nombreMenus(self):
        return len(self.menus())

    def descendreCurseur(self, event):
        """descend le curseur de 1 dans le menu"""
        if self.ligneCurseur < self.nombreMenus():
            self.ligneCurseur += 1
        else:
            self.ligneCurseur = 1

        self.curseur.grid(row=self.ligneCurseur, column=0)
        self.curseur.update()

    def monterCurseur(self, event):
        """monte le curseur de 1 dans le menu"""
        if self.ligneCurseur > 1:
            self.ligneCurseur -= 1
        else:
            self.ligneCurseur = self.nombreMenus()
        self.curseur.grid(row=self.ligneCurseur, column=0)
        self.curseur.update()

    def majContenu(self):
        """mets à jour les possibilitées de menus selon la connexion"""
        for menu in range(self.nombreMenus()):
            self.texteMenus[menu].destroy()

        self.joueur = joueurConnecte()
        self.texteMenus = majListe(self.joueur)

        for menu in range(len(self.texteMenus)):
            self.texteMenus[menu] = Label(master=self.canMenu, text=self.texteMenus[menu], font=('Helvetica', 20))
            self.texteMenus[menu].grid(row=menu+1, column=1, pady=10, sticky=W)

        self.title(majEntete(self.joueur))

    def menu(self, event):
        self.menu = self.ligneCurseur-1

        #contrôle qu'aucune fenêtre satellite n'est ouverte
        if self.peutOuvrir:
            #selon le curseur on lance le menu correspondant
            if self.menu == 0:
                self.destroy()

                jeu = Jeu()
                jeu.focus_force()
                jeu.mainloop()

                accueil = Accueil()
                accueil.focus_force()
                accueil.mainloop()

            elif self.menu == 1:
                if estConnecte(self.joueur):
                    deconnexion(fichierJoueur)
                    self.majContenu()
                else:
                    self.peutOuvrir = False
                    Inscription(self, geometryPetite, "Inscription", "p").focus()

            elif self.menu == 2:
                self.peutOuvrir = False
                Regles(self, "Règles", "p").focus()

            elif self.menu == 3:
                self.peutOuvrir = False
                Commandes(self, "Commandes", "p").focus()

            elif self.menu == 4:
                self.peutOuvrir = False
                MeilleursScores(self, "Meilleurs Scores", "g").focus()

            elif self.menu == 5:
                self.destroy()
