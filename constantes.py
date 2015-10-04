# -*- coding: utf-8 -*-

###############################
#Constantes pour le jeu tetris#
###############################

from tetris import *
from classes import *
from fonctions import *

#résolution de la fenêtre principales
#####################################

largeur_fenetre = 820
hauteur_fenetre = 780

#résolution du jeu
##################

largeur_canevas = 380
hauteur_canevas = 760

cote_carre = 38

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