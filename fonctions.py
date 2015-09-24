# -*- coding: utf-8 -*-

##############################
#Fonctions pour le jeu tetris#
##############################

from tetris import *
from classes import *
from constantes import *

def quitter(continuer):
    pygame.display.quit()
    continuer = False