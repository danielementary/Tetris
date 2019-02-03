# -*- coding: utf-8 -*-

from bloc import *

import sys
sys.path.insert(0, "..")
sys.path.insert(0, "classesMenu")

class Piece():
    def __init__(self, grille):
        self.carre_ref_ligne = 0
        self.carre_ref_colonne = 4
        self.grille = grille

    def descente_noview(self):
        """fait descendre la pièce sans l'afficher, jusqu'à qu'elle ne puisse plus"""
        if self.check_descente():
            for i in range(len(self.blocs)):
                self.blocs[i].descente()
                self.carre_ref_ligne += 1

    def check_descente(self):
        """contrôle que la(es) case(s) sous les blocs de la pièce soient libres, Return True(libres) ou False(occupées)"""
        a = 1
        for i in range(len(self.blocs)):
            if not self.blocs[i].check_descente():
                a = 0
        if a:
            return True
        else:
            return False

    def descente(self):
        """applique la méthode descente de blocs à chacuns des blocs de la pièce pour la faire descendre si elle le peut"""
        if self.check_descente():
            for i in range(len(self.blocs)):
                self.blocs[i].descente()
            self.carre_ref_ligne += 1

    def check_lateral(self, sens):
        """contrôle que la(es) case(s) à gauche ou à droite de la pièce sont libres, sens ("g" ou "d") détermine le côté"""
        a = 1
        for i in range(len(self.blocs)):
            if not self.blocs[i].check_lateral(sens):
                a = 0
        if a:
            return True
        else:
            return False

    def lateral(self,sens):
        """applique la méthode latéral à chaque blocs de la pièce dans la direction (sens) souhaité ("g" ou "d") si elle le peut"""
        if self.check_lateral(sens):
            for i in range(len(self.blocs)):
                self.blocs[i].lateral(sens)
        if sens == 'd':
            self.carre_ref_colonne += 1
        if sens == 'g':
            self.carre_ref_colonne -= 1

    def fixer(self):
        """fixe chaque bloc de la pièce dans le jeu"""
        for i in range(len(self.blocs)):
            self.blocs[i].fixer(self.grille)

    def check_tourner(self):
        """contrôle que les cases qu'occuperont les blocs de la pièce une fois celle-ci tournée soient libres"""
        if self.pos<(len(self.positions)-1):
            pos_suivante=self.pos + 1
        else:
            pos_suivante = 0

        for i in range(len(self.positions[pos_suivante])):
            for j in range(len(self.positions[pos_suivante][i])):
                if self.positions[pos_suivante][i][j]:
                    if (self.carre_ref_ligne + (i-1)) < 0 or \
                            (self.carre_ref_ligne + (i-1)) > 21 or \
                            (self.carre_ref_colonne + (j-1)) < 0 or \
                            (self.carre_ref_colonne + (j-1)) > 9:
                        return False

                    elif (self.carre_ref_ligne + (i-1)) > 0 and \
                            (self.carre_ref_ligne + (i-1)) < 21 and \
                            (self.carre_ref_colonne + (j-1)) > 0 and \
                            (self.carre_ref_colonne + (j-1)) < 9:
                        if self.grille.grille[(self.carre_ref_ligne + (i-1))][(self.carre_ref_colonne + (j-1))] != 0:
                            return False
        return True

    def tourner(self):
        """fait tourner la pièce dans le sens horaires"""
        if self.check_tourner():
            if self.pos<(len(self.positions)-1):
                self.pos+=1
            else:
                self.pos=0
            a=0
            for i in range(len(self.positions[self.pos])):
                for j in range(len(self.positions[self.pos][i])):
                    if self.positions[self.pos][i][j] :
                        self.blocs[a].deplacer(self.carre_ref_ligne + (i-1), self.carre_ref_colonne + (j-1))
                        a+=1
