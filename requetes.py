# -*- coding: utf-8 -*-

###################
# Fichier du SGBD #
###################

#importations
#############

import sqlite3

#tables de base de données
##########################

#joueur
#######

reqPlayer = """CREATE TABLE Player(PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
                Pseudo VARCHAR(10) NOT NULL, Password VARCHAR(25) NOT NULL,
                CreationDate DATETIME NOT NULL)"""

#partie
#######

reqScore = """CREATE TABLE Score(ScoreID INTEGER PRIMARY KEY AUTOINCREMENT,
                Level INTEGER NOT NULL, ScoreDate DATETIME NOT NULL,
                Points INTEGER NOT NULL, Lines INTEGER NOT NULL,
                PlayerID INTEGER NOT NULL,
                FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID))"""

#fonctions du SGBD
##################

def connexionDB(fichierDB):
    """connexionDB(string fichierDB) --> connexion et curseur.
    ouvre la connexion avec la DB et crée le curseur et change le row_factory
    """
    conn = sqlite3.connect(fichierDB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    return conn, cur

def deconnexionDB(conn, cur):
    """deconnexionDB(conn, cur)--> none
    effectue les modifications et ferme le curseur et la connexion avec la DB
    """
    conn.commit()
    cur.close()
    conn.close()

def executeurDeRequetes(cur, liste, type):
    """executeurDeRequetes(cur, list liste, int type)--> Bool, liste or row
    execute les requêtes de la liste de requete <liste>, retourne soit un Bool, soit une liste de row soit un row en fct de <type>
    """
    for requete in liste:
        cur.execute(requete)

    #pour une requête de type existe-t-il ?
    if type == 1:
        if len(list(cur)) >= 1:
            return True

    #pour une requête du type récolter plusieurs infos
    elif type == 2:
        lignesListe = []

        for l in cur:
            lignesListe.append([l[0], l[1],l[2]])

        return lignesListe

    #pour une requête du type récolter la première info
    elif type == 3:
        ligne = cur.fetchone()

        return ligne[0]
