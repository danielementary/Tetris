# -*- coding: utf-8 -*-

#################################
#Fichier principal du jeu tetris#
#################################

from tkinter import *

#from classes import *
from constantes import *
from fonctions import *

from classesApp import *

menu = 6

if menu == 0:
    accueil = Accueil(fondPrincipal=fondPrincipal, geometry=geometry,
                      texteMenus=texteMenus)
    accueil.mainloop()
    
if menu == 6:
    jeu = Jeu(fondPrincipal=fondPrincipal, geometry=geometry,
                largeur_canevas=largeur_canevas,
                hauteur_canevas=hauteur_canevas,
                fondCadres=fondCadres)
    jeu.mainloop()