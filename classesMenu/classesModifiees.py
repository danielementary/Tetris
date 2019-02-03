# -*- coding: utf-8 -*-

##################################
#Classes principales pour le jeu #
##################################

from tkinter import *

import sys
sys.path.insert(0, "..")

from constantes import *

#classes modifiées
##################

class FenetreGrande(Tk):

    def __init__(self, geometry, pseudoJoueur, **Arguments):
        Tk.__init__(self, **Arguments)
        self.geometry(geometry)
        self.resizable(width=FALSE, height=FALSE)
        self.title(pseudoJoueur)
        self.tk_setPalette(background="light sky blue", foreground="black")

class FenetrePetite(Toplevel):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        Toplevel.__init__(self, parent, **Arguments)
        self.geometry(geometryPetite)
        self.resizable(width=FALSE, height=FALSE)
        self.protocol('WM_DELETE_WINDOW', self.quitter)

        self.parent = parent
        self.bind('<Escape>', self.quitter)


        if gridOuPack == "g":
            Label(self, text=titre, font=("Helvetica", 20)).grid(column=1, row=1, columnspan=2)
        else:
            Label(self, text=titre, font=("Helvetica", 20)).pack(side=TOP, pady=10)

    def quitter(self, event=None):
        """fonction destroy modifiée pour remettre peutOuvrir à true quand on ferme une fenêtre satellite"""
        self.parent.peutOuvrir = True
        self.destroy()
