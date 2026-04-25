# -*- coding: utf-8 -*-

###############################
# Fichier de lancement du jeu #
###############################

#importations
#############

import os
from constantes import *
from classesMenu.accueil import Accueil

#création de la base de données
###############################

if not os.path.isfile(fichierDB):                       #création s'il n'éxiste pas du fichier de BD
    conn, cur = connexionDB(fichierDB)                  #connexion à la BD
    executeurDeRequetes(cur, [reqPlayer, reqScore], 0)  #remplissage de la BD
    deconnexionDB(conn, cur)                            #déconnexion de la BD

#création de l'accueil
######################


deconnexion(fichierJoueur)                              #déconnexion du joueur éventuellement connectée avant le lancement du jeu

jouerDeLaMusique()

Accueil(geometry=geometry,texteMenus=majListe(None),  #création de l'Accueil
        pseudoJoueur=majEntete(None)).mainloop()
