# -*- coding: utf-8 -*-

##################
# accueil du jeu #
##################

from tkinter import *
from tkinter.messagebox import *

from classesModifiees import *
from commandes import *
from connexion import *
from inscription import *
from jeu import *
from meilleursScores import *
from regles import *

import sys
sys.path.insert(0, "..")

from constantes import *
from fonctionsConnexion import *

class Accueil(FenetreGrande):

    def __init__(self, geometry, texteMenus, pseudoJoueur, **Arguments):
        FenetreGrande.__init__(self, geometry, pseudoJoueur, **Arguments)

        self.joueur = nomJoueur(fichierJoueur)
        self.texteMenus = texteMenus

        self.canTitre = Canvas(master=self, height=130, width=largeur)
        self.canTitre.create_text(largeur/2, 75, text="Tetris", font=('Helvetica', 90))
        self.canTitre.grid(row=1,column=0, columnspan=2, pady=10)

        self.canMenu = Canvas(master=self, height=hauteur-130, width=largeur)
        self.canMenu.grid(row=2, column=1)

        for menu in range(len(self.texteMenus)):
            self.texteMenus[menu] = Label(master=self.canMenu, text=self.texteMenus[menu], font=('Helvetica', 20))
            self.texteMenus[menu].grid(row=menu+1, column=1, pady=10, sticky=W)

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
        self.bind('<Return>', self.menu)
        self.bind('<Button-1>', self.alerte)

    def descendreCurseur(self, event):
        """descend le curseur de 1 dans le menu"""
        if self.ligneCurseur < len(self.texteMenus):
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
            self.ligneCurseur = len(self.texteMenus)
        self.curseur.grid(row=self.ligneCurseur, column=0)
        self.curseur.update()

    def alerte(self, event):
        """affiche une pop up indiquant d'utiliser le clavier"""
        showinfo("Matériel", "Les flèches du clavier sont plus utiles que la souris ! (Et ça fait pro ;) )")

    def majContenu(self):
        """mets à jour les possibilitées de menus selon la connexion"""
        for menu in range(len(self.texteMenus)):
            self.texteMenus[menu].destroy()

        self.joueur = nomJoueur(fichierJoueur)
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
                if estConnecte(self.joueur):
                    self.destroy()
                    jeu = Jeu(geometry=geometry, pseudoJoueur=majEntete(self.joueur))
                    jeu.focus_force()
                    jeu.mainloop()

                    acc = Accueil(geometry=geometry,texteMenus=majListe(self.joueur),
                            pseudoJoueur=majEntete(self.joueur))
                    acc.focus_force()
                    acc.mainloop()
                else:
                    self.peutOuvrir = False
                    Connexion(self, geometryPetite, "Connexion", "p").focus()

            elif self.menu == 1:
                if estConnecte(self.joueur):
                    deconnexion(fichierJoueur)
                    self.majContenu()
                else:
                    self.peutOuvrir = False
                    Inscription(self, geometryPetite, "Inscription", "p").focus()

            elif self.menu == 2:
                self.peutOuvrir = False
                Regles(self, geometryPetite, "Règles", "p").focus()

            elif self.menu == 3:
                self.peutOuvrir = False
                Commandes(self, geometryPetite, "Commandes", "p").focus()

            elif self.menu == 4:
                self.peutOuvrir = False
                MeilleursScores(self, geometryPetite, "Meilleurs Scores", "g").focus()

            elif self.menu == 5:
                self.destroy()
