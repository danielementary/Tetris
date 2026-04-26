# -*- coding: utf-8 -*-

###############################
# Fichier de lancement du jeu #
###############################

#importations
#############
from utilitaires import jouerDeLaMusique, demarrerManette
from sgbd import creerDB
from joueur import connexionInitiale

from classesMenu.accueil import Accueil

#lancement de la musique et de la manette
#########################################
jouerDeLaMusique()
demarrerManette()

#création de la base de données
###############################
creerDB()

#conexion du joueur
###################
connexionInitiale()

#lancement de l'interface
#########################
Accueil().mainloop()
