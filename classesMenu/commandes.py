# -*- coding: utf-8 -*-

###################
#Commandes du jeu #
###################

from tkinter import *

import sys
sys.path.insert(0, "..")

from constantes import *

from classesModifiees import FenetrePetite

class Commandes(FenetrePetite):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        FenetrePetite.__init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments)

        for tuple in texteCommandes:
            Label(self, text="{} : {}".format(tuple[0], tuple[1]), wraplength=250,
             font=('Helvetica', 10)).pack(side=TOP, anchor=W)
