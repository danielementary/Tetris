# -*- coding: utf-8 -*-

##############################
#Fonctions pour le jeu tetris#
##############################

from tetris import *
from classes import *
from constantes import *


def quitter(continuer):
    """quitter(bool continuer) ---> return none
    ferme la boucle principale et quitte la fenêtre"""
    pygame.display.quit()
    continuer = False
    
def afficher_menu(fenetre):
    for ligne in range(len(texteAcc)):
        label = policeAcc.render(texteAcc[ligne], 1, bleu_5)
        fenetre.blit(label, (100, espacement*(1/2 + ligne)))