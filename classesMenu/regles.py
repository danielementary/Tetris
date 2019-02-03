# -*- coding: utf-8 -*-

################
#Règles du jeu #
################

from tkinter import *

from classesModifiees import FenetrePetite

class Regles(FenetrePetite):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        FenetrePetite.__init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments)
        reglesTxt = Label(self, text="Ne fais pas semblant, tout le monde connait les règles de ce jeu mythique !",
                            wraplength=250, font=('Helvetica', 10))
        reglesTxt.pack(side=TOP)
