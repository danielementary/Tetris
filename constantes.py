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

largeur_fenetre = 680
hauteur_fenetre = 680

geometry = "{}x{}+400+100".format(largeur_fenetre, hauteur_fenetre)

#résolution du jeu
##################

largeur_canevas = 330
hauteur_canevas = 660

cote_carre = 26

#fréquence de rafraîchissment
#############################

hz = 60

#dictionnaire de menus
######################

menus = {0: "accueil", 1: "règles", 2: "commandes", 3: "inscription",
         4: "connexion", 5: "meilleurs scores", 6: "nouvelle partie",
         7: "quitter"}

texteMenus = []
for touche, titre in menus.items():
    texteMenus.append("{} - {}".format(touche, titre))


#couleurs
#########

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
couleur_biais = "red"
couleur_biaisi = "green"