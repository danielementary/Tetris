# -*- coding: utf-8 -*-

##################################
#Classes principales pour le jeu #
##################################

from tkinter import *

from classes import *
from constantes import *
from fonctions import *

class Jeu(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.config(bg=fondPrincipal)
        self.geometry(geometry)
        self.resizable(width=FALSE, height=FALSE)

        self.cadreTetris = Canvas(master=self, width=largeur_canevas, 
                                    height=hauteur_canevas, bg=fondCadres)
        self.cadreTetris.grid(row=0, rowspan=2, column=1, padx=10, pady=10)

        self.cadrePieces = Canvas(master=self, width="260", height="250", bg=fondCadres)
        self.cadrePieces.grid(row=0, column=2, padx=80, pady=100)

        self.cadreScores = Canvas(master=self, width="260", height="300", bg=fondCadres)
        self.cadreScores.grid(row=1, column=2, padx=80, pady=75)
        
##### Programme principal #####
Jeu().mainloop()