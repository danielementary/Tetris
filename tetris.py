# -*- coding: utf-8 -*-

#################################
#Fichier principal du jeu tetris#
#################################

from tkinter import *

from classes import *
from constantes import *
from fonctions import *

class Jeu(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.canevas = Canvas(master=self, width=largeur_fenetre, height=hauteur_fenetre, bg=gris)

##### Programme principal #####
Jeu().mainloop()