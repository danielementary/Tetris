# -*- coding: utf-8 -*-

#################################
#Fichier principal du jeu tetris#
#################################

from tkinter import *

from classes import *
from constantes import *
from fonctions import *

from classesApp import *

class Application(Tk):
    
    jeu = Jeu()
    jeu.mainloop()

##### Programme principal #####
Application().mainloop()