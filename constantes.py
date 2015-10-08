# -*- coding: utf-8 -*-

###############################
#Constantes pour le jeu tetris#
###############################

from tkinter import *

from classesApp import *
#from classes import *
from fonctions import *

#résolution de la fenêtre principales
#####################################

largeur_fenetre = 600
hauteur_fenetre = 560

geometry = "{}x{}".format(largeur_fenetre, hauteur_fenetre)

#résolution du jeu
##################

largeur_canevas = 260
hauteur_canevas = 572

cote_carre = 26

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


#couleurs (rgb)
###############

blanc = "#252525"
gris = "#202020"
noir = "#101010"

fondPrincipal = "light sky blue"
fondCadres = "light yellow"