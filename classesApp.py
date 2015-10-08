# -*- coding: utf-8 -*-

##################################
#Classes principales pour le jeu #
##################################

from tkinter import *

#from classes import *
from fonctions import *
from constantes import *

class Jeu(Tk):
    
    class Jeu(Tk):
    
    def __init__(self, fondPrincipal, geometry, largeur_canevas,
                 hauteur_canevas, fondCadres):
        Tk.__init__(self)
        self.config(bg=fondPrincipal)
        self.geometry(geometry)
        self.resizable(width=FALSE, height=FALSE)

        self.cadreTetris = Canvas(master=self, width=largeur_canevas,
                                  height=hauteur_canevas, bg=fondCadres)
        self.cadreTetris.grid(row=0, rowspan=3, column=1, padx=5, pady=10)

        self.cadrePieces = Canvas(master=self, width="240", height="240", bg=fondCadres)
        self.cadrePieces.grid(row=0, column=2, columnspan=2, padx=50, pady=10)

        self.cadreScores = Canvas(master=self, width="240", height="260", bg=fondCadres)
        self.cadreScores.grid(row=1, column=2, columnspan=2, padx=50, pady=10)

        self.boutonQuitter = Button(master=self, text="Quitter")
        self.boutonQuitter.grid(row=2, column=2, pady=30)

        self.boutonPause = Button(master=self, text="Pause")
        self.boutonPause.grid(row=2, column=3, pady=30)