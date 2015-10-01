# -*- coding: utf-8 -*-

############################
#Classes pour le jeu tetris#
############################

from tetris import *
from constantes import *
from fonctions import *

class Piece(object):
    #position de référence de chaque pièce [x,y]
    pos = [5, -3]


def tourner(self):
    pass


class Grille():
    def __init__(self):
        
        self.grille=[]
        
        for i in range(20):
            self.grille.append([0,0,0,0,0,0,0,0,0,0])
    
    def check_vide(self,ligne, colonne):
        """retourne TRUE si la case est vide, FALSE sinon
            ligne et colonne commencent a 0"""
        
        if self.grille[ligne][colonne]==0:
            return True
        else:
            return False
            
    def remplir_case(self, ligne, colonne):
        """permutte le 0 en 1 à la case souhaitée par ligne et colonne qui commencent a 0"""
        
        self.grille[ligne][colonne]=1
     


class Blocs():
    def __init__(self,couleur, numero_ligne, numero_colonne, canevas):
        
        #coordonnées sont celles du coin supérieur gauche et les numerotations de lignes et colonnes commencent a 0
        self.ligne=numero_ligne
        self.colonne=self.numero_colonne
        
        self.coordx=numero_ligne*cote
        self.coordy=numero_colonne*cote
        
        self.couleur=couleur
        
        self.cote=cote
        
        self.can=canevas
        
        
        self.can.create_rectangle(self.coordx, self.coordy, self.coordx + self.cote, self.coordy + self.cote, fill=self.couleur)
        
    def check_descente(self):
        """retourne TRUE si la case située sous le bloc est vide, FALSE sinon"""