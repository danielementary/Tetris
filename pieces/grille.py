# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "..")

from constantes import *

class Grille():
    def __init__(self):
        self.grille = []            #simulation de la grille par une liste de 9 listes de 9 éléments, 0 pour une case libre, "[couleur]" pour une occupée

        self.niveau = 1
        self.lignes = 0
        self.score = 0

        for i in range(22):
            self.grille.append([0,0,0,0,0,0,0,0,0,0])

    def remplir_case(self, ligne, colonne, couleur):
        """permutte le 0 en chaine de caractere, etant le nom de la couleur
        à la case souhaitée par ligne et colonne dont la numérotation
        commence à 0"""

        self.grille[ligne][colonne] = couleur

    def afficher(self, canevas):
        """affiche le jeu dans le canevas"""
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                if self.grille[i][j] != 0:
                    canevas.create_rectangle(j*cote_carre+2, i*cote_carre+1,
                                            j*cote_carre + cote_carre+2,
                                            i*cote_carre + cote_carre+1,
                                            fill=self.grille[i][j])

    def enleve_ligne_pleine(self):
        """enleve toutes les lignes pleines et les remplace par des lignes vides au debut"""
        i = 0
        compteur = 0

        while i < len(self.grille):
            flag = 1

            for j in range(len(self.grille[i])):
                if self.grille[i][j] == 0:
                    flag = 0

            if flag == 1:
                del(self.grille[i])
                self.grille = [[0,0,0,0,0,0,0,0,0,0]]+self.grille
                compteur += 1
                i = 0
                self.lignes += 1
            else:
                i += 1

        if compteur == 1:
            self.score += 40*self.niveau
        if compteur == 2:
            self.score += 100*self.niveau
        if compteur == 3:
            self.score += 300*self.niveau
        if compteur == 4:
            self.score += 1200*self.niveau
