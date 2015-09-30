# -*- coding: utf-8 -*-

############################
#Classes pour le jeu tetris#
############################

import pygame
from pygame.locals import *

from tetris import *
from constantes import *
from fonctions import *

class Piece(object):
    #position de référence de chaque pièce [x,y]
    pos = [5, -3]


def tourner(self):
    pass


class Blocs():
    def __init__(couleur, coordx, coordy):
        
        #coordonnées sont celles du coin supérieur gauche
        self.coordx=coordx
        self.coordy=coordy
        self.couleur=couleur
        self.cote=40
        
#class Barre(Piece):

#class Te(Piece):

#class Lambda(Piece):

#class Gamma(Piece):

#class BiaisZ(Piece):


#class BiaisS(Piece):
