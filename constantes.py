# -*- coding: utf-8 -*-

###############################
#Constantes pour le jeu tetris#
###############################

import pygame
from pygame.locals import *

from tetris import *
from classes import *
from fonctions import *

#résolution de la fenêtre principales
#####################################

largeur_fenetre = 830
hauteur_fenetre = 770

#fréquence de rafraîchissment
#############################

hz = 60

#dictionnaire de menus
######################

menus = {0: "accueil", 1: "règles", 2: "commandes", 3: "inscription",
         4: "connexion", 5: "meilleurs scores", 6: "nouvelle partie",
         7: "quitter"}

texteAcc = []
for touche, titre in menus.items():
    texteAcc.append("{} - {}".format(touche, titre))

espacement = hauteur_fenetre / len(texteAcc)

#polices
########
pygame.font.init()
policeAcc = pygame.font.SysFont(None, 40)

#couleurs (rgb)
###############

blanc = (255, 255, 255)
gris = (200, 200, 200)
noir = (10, 10, 10)

bleu_1 = (205, 219, 255)
bleu_2 = (53, 110, 255)
bleu_3 = (42, 88, 204)
bleu_4 = (25, 52, 122)
bleu_5 = (34, 60, 127)

baton_turq = (72, 255, 237)
cube_jaune = (255, 208, 40)
te_violet = (140, 60, 255)
lambda_orange = (232, 131, 25)
gamma_bleu = (12, 38, 232)
biais_rouge = (232, 37, 40)
biais_vert = (39, 255, 46)


#position des éléments de l'interface
#####################################

#rectangles: (posX, posY, largeur, hauteur)

#taille d'une case de la grille virtuelle de jeu en px

cote=40

#canvas où tombent les pièces
jeuCanPos = (10, cote*10 , cote*20)
#canvas qui affiche la prochaine pièce
pieceCanPos = (440, 15, 300, 300)