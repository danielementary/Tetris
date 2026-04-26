# -*- coding: utf-8 -*-

###################
# Fichier du SGBD #
###################

#importations
#############
import os
import sqlite3
from constantes import listeJoueurs

#fichier de la base de données
##############################
fichierDB = "BaseDeDonnees.sq3"

#fonctions
##########
def creerDB():
    """creerDB() --> None
    crée la base de données si elle n'existe pas et crée les tables de base de données et peuple la table Player avec la liste de joueurs s'ils ne sont pas dedans
    """
    db_existe = os.path.isfile(fichierDB)
    conn, cur = connexionDB(fichierDB)

    if not db_existe:
        cur.execute("""CREATE TABLE Player(
            PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Pseudo   VARCHAR(10) NOT NULL UNIQUE
        )""")
        cur.execute("""CREATE TABLE Score(
            ScoreID   INTEGER  PRIMARY KEY AUTOINCREMENT,
            Level     INTEGER  NOT NULL,
            ScoreDate DATETIME NOT NULL,
            Points    INTEGER  NOT NULL,
            Lines     INTEGER  NOT NULL,
            PlayerID  INTEGER  NOT NULL,
            FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)
        )""")

    cur.execute("SELECT Pseudo FROM Player")
    existants = [row[0] for row in cur.fetchall()]
    for joueur in listeJoueurs:
        if joueur not in existants:
            cur.execute("INSERT INTO Player(Pseudo) VALUES(?)", (joueur,))

    deconnexionDB(conn, cur)

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

