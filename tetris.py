# -*- coding: utf-8 -*-

#################################
#Fichier principal du jeu tetris#
#################################

from tkinter import *

#from classes import *
from constantes import *
from fonctions import *

from classesApp import *

jeu = Jeu(fondPrincipal=fondPrincipal, geometry=geometry,
          largeur_canevas=largeur_canevas,
          hauteur_canevas=hauteur_canevas,
          fondCadres=fondCadres)
jeu.mainloop()