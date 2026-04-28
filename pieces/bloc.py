# -*- coding: utf-8 -*-
from constantes import cote_carre
from .grille import Grille

class Bloc():
    def __init__(self, couleur, ligne, colonne, canevas, grille):
        self.ligne   = ligne
        self.colonne = colonne
        self.grille  = grille
        self.coordx  = self.colonne * cote_carre
        self.coordy  = self.ligne   * cote_carre
        self.couleur = couleur
        self.cote    = cote_carre
        self.can     = canevas
        self.bloc    = self.can.create_rectangle(
            self.coordx,           self.coordy,
            self.coordx + self.cote, self.coordy + self.cote,
            fill=self.couleur, outline="black")

    def check_descente(self):
        if self.ligne >= 21:
            return False
        return self.grille.grille[self.ligne + 1][self.colonne] == 0

    def check_lateral(self, sens):
        if sens == "d":
            if self.colonne >= 9:
                return False
            return self.grille.grille[self.ligne][self.colonne + 1] == 0
        if sens == "g":
            if self.colonne <= 0:
                return False
            return self.grille.grille[self.ligne][self.colonne - 1] == 0

    def descente(self):
        self.ligne  += 1
        self.coordy  = self.ligne * cote_carre
        self.can.coords(self.bloc,
            self.coordx,             self.coordy,
            self.coordx + self.cote, self.coordy + self.cote)

    def descente_noview(self):
        self.ligne += 1

    def lateral(self, sens):
        if sens == 'g':
            self.colonne -= 1
        elif sens == 'd':
            self.colonne += 1
        self.coordx = self.colonne * cote_carre
        self.can.coords(self.bloc,
            self.coordx,             self.coordy,
            self.coordx + self.cote, self.coordy + self.cote)

    def fixer(self, grille):
        grille.grille[self.ligne][self.colonne] = self.couleur

    def deplacer(self, new_ligne, new_colonne):
        self.ligne   = new_ligne
        self.colonne = new_colonne
        self.coordx  = self.colonne * cote_carre
        self.coordy  = self.ligne   * cote_carre
        self.can.coords(self.bloc,
            self.coordx,             self.coordy,
            self.coordx + self.cote, self.coordy + self.cote)
