# -*- coding: utf-8 -*-

###############################
#Constantes pour le jeu tetris#
###############################

#importations
#############
from tkinter import *
from fonctionsConnexion import *

import pygame

#résolution de l'écran
######################
geometry = "{}x{}+{}+{}".format(640, 480, 0, 0)

#résolution de la fenêtre secondaire
####################################
geometryPetite = "{}x{}+{}+{}".format(320, 240, 160, 120)

#résolution du jeu
##################

cote_carre = 25

largeur_canevas = cote_carre*10+1
hauteur_canevas = cote_carre*22

hauteurCanPieces = 180
largeurCanPieces = cote_carre*6

#fichiers
#########

fichierDB = "BaseDeDonnees.sq3"
fichierJoueur = "joueur.txt"

#commandes
##########

texteCommandes = [
("Flèche haute", "Tourner la pièce"),
("Flèches bas", "Accélérer la chute"),
("Flèche gauche", "Déplacer la pièce vers la gauche"),
("Flèche droite", "Déplacer la pièce vers la droite"),
("Espace", "Faire tomber la pièce d'un coup"),
("Escape", "Mettre le jeu en pause"),
("m", "Lance ou coupe la musique")
]

#couleurs
#########

bgCouleur="white"
blanc = "white"
gris = "gray"
noir = "black"
fondPrincipal = "dark slate blue"
fondCadres = "ivory"
couleur_bouton = "navy"
couleur_barre = "turquoise1"
couleur_carre = "yellow"
couleur_te = "purple"
couleur_lambda = "orange"
couleur_gamma = "blue"
couleur_S = "red"
couleur_Z = "green"


def jouerDeLaMusique():
    pygame.mixer.init()
    print(pygame.mixer.get_init())
    pygame.mixer.music.load("classesMenu/Tetris.wav")
    pygame.mixer.music.play(-1)

