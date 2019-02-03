# -*- coding: utf-8 -*-

###############################
# Fichier de lancement du jeu #
###############################

#importations
#############

import os
import sqlite3
from constantes import *
from requetes import *
from tkinter import *
from fonctionsConnexion import *
import sys
sys.path.insert(0, "classesMenu") 						#modification du chemin relatif
from accueil import *

#création de la base de données
###############################

if not os.path.isfile(fichierDB):                       #création s'il n'éxiste pas du fichier de BD
    conn, cur = connexionDB(fichierDB)                  #connexion à la BD
    executeurDeRequetes(cur, [reqPlayer, reqScore], 0)  #remplissage de la BD
    deconnexionDB(conn, cur)                            #déconnexion de la BD

#création de l'accueil
######################


deconnexion(fichierJoueur)                              #déconnexion du joueur éventuellement connectée avant le lancement du jeu

joueur = nomJoueur(fichierJoueur)                       #connexion du joueur (aucun joueur)

Accueil(geometry=geometry,texteMenus=majListe(joueur),  #création de l'Accueil
        pseudoJoueur=majEntete(joueur)).mainloop()
