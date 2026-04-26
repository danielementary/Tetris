# -*- coding: utf-8 -*-

##############################
# Gestion du joueur connecté #
##############################

#importations
#############
from constantes import listeJoueurs

#fichier du joueur connecté
###########################
fichierJoueur = "joueur.txt"

#fonctions
##########
def connexion(joueur):
    if joueur not in listeJoueurs:
        joueur = listeJoueurs[-1]
    with open(fichierJoueur, "w") as fichier:
        fichier.write(joueur)

def connexionInitiale():
    connexion(listeJoueurs[0])

def connexionInvite():
    connexion(listeJoueurs[-1])

def joueurConnecte():
    try:
        with open(fichierJoueur, "r") as fichier:
            joueur = fichier.read()
            if joueur not in listeJoueurs:
                return listeJoueurs[-1]
            else:
                return joueur
    except:
        return listeJoueurs[-1]
        
