# -*- coding: utf-8 -*-

############################
#Classes pour le jeu tetris#
############################

from tkinter import *

from classesApp import *
from fonctions import *
from constantes import *

class Piece(object):
    #position de référence de chaque pièce [x,y]
    pos = [5, -3]


    def tourner(self):
        pass


class Grille():
    def __init__(self):
        
        self.grille=[]
        
        for i in range(22):
            self.grille.append([0,0,0,0,0,0,0,0,0,0])
    
    def check_vide(self,ligne, colonne):
        """retourne TRUE si la case est vide, FALSE sinon
            ligne et colonne commencent a 0"""
        
        if self.grille[ligne][colonne]==0:
            return True
        else:
            return False
            
    def remplir_case(self, ligne, colonne, couleur):
        """permutte le 0 en 1,2,3,4,5 ou 6 en fct de la couleur
        à la case souhaitée par ligne et colonne dont la numérotation
        commence a 0"""
        
        self.grille[ligne][colonne]=couleur
     


class Bloc():
    
    def __init__(self,couleur, ligne, colonne, canevas):
        
        #coordonnées sont celles du coin supérieur gauche et les numerotations 
        #de lignes et colonnes commencent a 0
        
        self.ligne=ligne
        self.colonne=colonne
        
        self.coordx=self.ligne*cote
        self.coordy=self.colonne*cote
        
        self.couleur=couleur
        
        self.cote=cote
        
        self.can=canevas
        
        
        self.can.create_rectangle(self.coordx, self.coordy, self.coordx + 
        self.cote, self.coordy + self.cote, fill=self.couleur)
        
    def check_descente(self):
        """retourne TRUE si la case située sous le bloc est vide, FALSE sinon"""
        
        if self.grille[self.ligne+1][self.colonne]!=0 or self.ligne+1>22:
            return False
        else:
            return True
            
    def check_lateral(self, sens):
        """return TRUE si la case a "sens" ("g" pour gauche ou "d" pour droite)
        est vide FALSE sinon"""
        
        if sens == "d":
            if self.grille[self.ligne][self.colonne+1]!=0 or self.colonne>=10:
                return False
            else:
                True
                
        if sens=="g":
            if self.grille[self.ligne][self.colonne-1]!=0 or self.colonne<0:
                return False
            else:
                True
        
    def descente(self):
        
        self.ligne+=1
        
        

class T():
    def __init__(self):
        
        self.bloc1 = Bloc(couleur="red", ligne=0, colonne=3, canevas=0)
        self.bloc_reference = Bloc(couleur="red", ligne=0, colonne=4, canevas=0)
        #le bloc de reference est celui que ne bouge pas lors des rotations
        
        self.bloc3 = Bloc(couleur="red", ligne=0, colonne=5, canevas=0 )
        self.bloc4 = Bloc(couleur="red",ligne=1, colonne=4, canevas=0 )
        
        
        self.sens=1                                 #sens peut valoir 1,2,3,4
        
    def tourner(self, sens):
        if sens == 1:
            pass
        #il faut passer au 2
        
            #if self.
            
            #self.bloc1.ligne-=1
            #self.bloc1.colonne+=1
        
        if sens == 2:
            pass
        
            #if grille[self.bloc_reference.ligne-1][self.bloc_reference.colonne]==0 and self.bloc_reference.ligne > 0: