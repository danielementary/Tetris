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
        self.canevas = Canvas(self, bg=gris, height=hauteur_fenetre, 
                                width=largeur_fenetre)
        print(largeur_fenetre, hauteur_fenetre)
        menu(self)

##### Programme principal #####
Jeu().mainloop()