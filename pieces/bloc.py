# -*- coding: utf-8 -*-

from grille import *

import sys
sys.path.insert(0, "..")

from constantes import *

class Bloc():

    def __init__(self,couleur, ligne, colonne, canevas, grille):

        #coordonnées sont celles du coin supérieur gauche et les numerotations
        #de lignes et colonnes commencent a 0

        self.ligne=ligne
        self.colonne=colonne
        self.grille=grille

        self.coordx=self.colonne*cote_carre
        self.coordy=self.ligne*cote_carre
        self.couleur=couleur

        self.cote=cote_carre

        self.can=canevas
        self.bloc=self.can.create_rectangle(self.coordx+2, self.coordy+1, self.coordx+
        self.cote+2, self.coordy+self.cote+1, fill=self.couleur)

    def check_descente(self):
        """retourne TRUE si la case située sous le bloc est vide, FALSE sinon"""

        if  self.ligne>22:
            return False
        elif self.ligne<21:
            if self.grille.grille[self.ligne+1][self.colonne]==0:
                return True
            else:
                return False
        else:
            return False

    def check_lateral(self, sens):
        """return TRUE si la case a "sens" ("g" pour gauche ou "d" pour droite)
        est vide FALSE sinon"""

        if sens == "d":
            if self.colonne>=9:
                return False
            if self.colonne<=8:
                if self.grille.grille[self.ligne][self.colonne+1]==0:
                    return True
                else:
                    return False

        if sens=="g":
            if self.colonne<=0:
                return False
            if self.colonne>=1:
                if self.grille.grille[self.ligne][self.colonne-1]==0:
                    return True
                else:
                    return False

    def descente(self):
        """fait descendre le blocs de une hauteur de bloc [cote_carre] et le redessine à sa nouvelle place"""

        self.ligne+=1
        self.coordy=self.ligne*cote_carre
        self.can.coords(self.bloc, self.coordx+2, self.coordy+1, self.coordx+
        self.cote+2, self.coordy+self.cote+1)

    def descente_noview(self):
        """descend le bloc d'une ligne sans le redessiner"""
        self.ligne+=1

    def lateral(self, sens):
        """deplace le bloc de [cote_carre] vers le "sens" ("g" ou "d")"""
        if sens=='g':
            self.colonne-=1
            self.coordx=self.colonne*cote_carre
            self.can.coords(self.bloc, self.coordx+2, self.coordy+1, self.coordx+
            self.cote+2, self.coordy+self.cote+1)
        if sens=='d':
            self.colonne+=1
            self.coordx=self.colonne*cote_carre
            self.can.coords(self.bloc, self.coordx+2, self.coordy+1, self.coordx+
            self.cote+2, self.coordy+self.cote+1)

    def fixer(self, grille):
        """remplit la grille à la case correspondante avec la couleur du bloc"""
        grille.grille[self.ligne][self.colonne]=self.couleur

    def deplacer(self, new_ligne, new_colonne):
        """deplace un bloc à une ligne new_ligne et une colonne new_colonne"""
        self.ligne=new_ligne
        self.colonne=new_colonne
        self.coordx=self.colonne*cote_carre
        self.coordy=self.ligne*cote_carre
        self.can.coords(self.bloc, self.coordx+2, self.coordy+1, self.coordx+
        self.cote+2, self.coordy+self.cote+1)
