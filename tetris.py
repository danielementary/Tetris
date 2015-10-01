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
        self.canevas = Canvas(self, bg=constantes.gris, 
                                height=constantes.hauteur_fenetre, 
                                width=constantes.largeur_fenetre)
        menu(self)

##### Programme principal #####
Jeu().mainloop()