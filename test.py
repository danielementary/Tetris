# -*- coding: utf-8 -*-

#############################
#Canevas de jeu test tetris #
#############################

from tkinter import *

from classes import *
from constantes import *
from fonctions import *

class Jeu(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="light sky blue")
        self.geometry("820x780")
        self.resizable(width=FALSE, height=FALSE)

        self.cadreTetris = Canvas(master=self, width="380", height="760", bg="light yellow")
        self.cadreTetris.grid(row=0, rowspan=2, column=1, padx=15, pady=10)

        self.cadrePieces = Canvas(master=self, width="190", height="150", bg="light yellow")
        self.cadrePieces.grid(row=0, column=2, padx=110, pady=40)

        self.cadreScores = Canvas(master=self, width="190", height="210", bg="light yellow")
        self.cadreScores.grid(row=1, column=2, padx=110, pady=120)
        
##### Programme principal #####
Jeu().mainloop()
