# -*- coding: utf-8 -*-

##################################
#Fichier principal du jeu tetris#
##################################

import pygame
from pygame.locals import *

from classes import *
from constantes import *

#initialisation de la fenêtre principale
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
#remplissage de la fenêtre
fenetre.fill(gris)
#mise à jour de tout l'écran
pygame.display.flip()

#initialisation de la police
pygame.font.init()

continuer = True
menu = 1

#boucle principale
while continuer:
    #limitation du rafraîchissement
    pygame.time.Clock().tick(hz)

    if menu == 1:
        while 1:
            #affichage de chaque possibilité
            for ligne in range(len(texteAcc)):
                label = policeAcc.render(texteAcc[ligne], 1, bleu_5)
                fenetre.blit(label, (100, espacement*(1/2 + ligne)))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    fenetre = pygame.display.quit()
                    continuer = False
