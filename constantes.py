# -*- coding: utf-8 -*-

###############################
#Constantes pour le jeu tetris#
###############################

from tetris import *
from classes import *
from fonctions import *

#résolution de la fenêtre principales
#####################################

largeur_fenetre = 830
hauteur_fenetre = 770

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

blanc = "#255255255"
gris = "#200200200"
noir = "#101010"

bleu_1 = "#205219255"
bleu_2 = "#53110255"
bleu_3 = "#4288204"
bleu_4 = "#2552122"
bleu_5 = "#3460127"

baton_turq = "#72255237"
cube_jaune = "#25520840"
te_violet = "#14060255"
lambda_orange = "#23213125"
gamma_bleu = "#1238232"
biais_rouge = "#2323740"
biais_vert = "#3925546"