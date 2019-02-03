# -*- coding: utf-8 -*-

###########################################################
# Fichier gérant les connexion et les mises à jour du jeu #
###########################################################

from requetes import *

def nomJoueur(fichierJoueur):
    """nomJoueur(string fichierJoueur)--> none or string
    ouvre le fichier <fichierJoueur> et retourne soit le joueur inscrit s'il y est soit rien et si le fichier
    n'existe pas, le crée
    """
    try:
        with open(fichierJoueur, "r") as fichier:
            joueur = fichier.read()
            if joueur == "":
                return None
            else:
                return joueur
    except:
        with open(fichierJoueur, "w") as fichier:
            return None

def idJoueur(fichierJoueur, fichierDB):
    """idJoueur(string fichierJoueur, string fichierDB)-->none or string
    ouvre le fichier <fichierJoueur> et le lit, s'il y a un joueur, ouvre la DB et récupère son enregistrement"""
    try:
        with open(fichierJoueur, "r") as fichier:
            joueur = fichier.read()
            if joueur == "":
                return None
            else:
                reqIdJoueur = """SELECT PlayerID
                                    FROM Player
                                    WHERE Pseudo = '{}'""".format(nomJoueur(fichierJoueur))
                conn, cur = connexionDB(fichierDB)
                id = executeurDeRequetes(cur, [reqIdJoueur], 3)
                deconnexionDB(conn, cur)

                return id
    except:
        with open(fichierJoueur, "w") as fichier:
            return None

def deconnexion(fichierJoueur):
    """deconnexion(string fichierJoueur) --> None
    nettoie le fichier <fichierJoueur> pour déconnecter le joueur"""
    with open(fichierJoueur, "w") as fichier:
        pass

def connexion(fichierJoueur, nomJoueur):
    """connexion(string fichierJoueur, string nomJoueur) --> None
    connecte le joueur en inscrivant le <nomJoueur> dans le fichier <fichierJoueur>
    """
    with open(fichierJoueur, "w") as fichier:
        fichier.write(nomJoueur)

def estConnecte(joueur):
    """estConnecte(string joueur) --> True si connecté False sinon"""
    if joueur == None:
        return False
    else:
        return True

def majEntete(joueur):
    """majEntete(string joueur) --> None
    Mise à jour de l'entête des fenêtes en fonction du nom du joueur
    """
    if estConnecte(joueur):
        return joueur
    else:
        return "Connecte-toi pour pouvoir jouer !"

def majListe(joueur):
    """majListe(string joueur) --> None
    Mise à jour de la liste des options disponibles dans le menu en fonction de la connexion
    """
    if estConnecte(joueur):
        return ["Nouvelle partie", "Deconnexion", "Règles", "Commandes",
        "Meilleurs scores", "Quitter"]
    else:
        return ["Connexion", "Inscription", "Règles", "Commandes",
        "Meilleurs scores", "Quitter"]
