# -*- coding: utf-8 -*-

#################################
#Fichier principal du jeu tetris#
#################################

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
menu = 0

#boucle principale
while continuer:
    #limitation du rafraîchissement
    pygame.time.Clock().tick(hz)
    
    #accueil
    if menu == 0:
        #affichage de chaque possibilité
        for ligne in range(len(texteAcc)):
            label = policeAcc.render(texteAcc[ligne], 1, bleu_5)
            fenetre.blit(label, (100, espacement*(1/2 + ligne)))
        
        pygame.display.flip()

    #règles
    if menu == 1:
        while 1:
            pass
      
    #commandes    
    if menu == 2:
        pass
    
    #inscriptions   
    if menu == 3:
        while 1:
            pass
    
    #connexion
    if menu == 4:
        while 1:
            pass
        
    #meilleurs scores   
    if menu == 5:
        pass
    
    #nouvelle partie
    if menu == 6:
        while 1:
            pass
    
    #quitter
    if menu == 7:
        while 1:
            pass
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quitter()