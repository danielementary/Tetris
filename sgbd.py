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

#fonctions du SGBD
##################
def connexionDB(fichierDB):
    """connexionDB(string fichierDB) --> connexion et curseur"""
    conn = sqlite3.connect(fichierDB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return conn, cur

def deconnexionDB(conn, cur):
    """deconnexionDB(conn, cur) --> None"""
    conn.commit()
    cur.close()
    conn.close()

#fonctions
##########
def creerDB():
    """creerDB() --> None
    crée la base de données si elle n'existe pas et peuple les joueurs manquants
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

def recupererScores():
    """Récupère le meilleur score de chaque joueur et les classe par ordre décroissant"""
    conn, cur = connexionDB(fichierDB)
    resultats = []
    for joueur in listeJoueurs:
        cur.execute("""
            SELECT MAX(Points), Lines FROM Score
            JOIN Player ON Score.PlayerID = Player.PlayerID
            WHERE Player.Pseudo = ?
        """, (joueur,))
        row = cur.fetchone()
        points = row[0] if row[0] is not None else 0
        lignes = row[1] if row[1] is not None else 0
        resultats.append((joueur, points, lignes))
    deconnexionDB(conn, cur)
    return sorted(resultats, key=lambda x: x[1], reverse=True)

def sauvegarderPartie(niveau, points, lignes, pseudo):
    """sauvegarderPartie(int niveau, int points, int lignes, string pseudo) --> None
    enregistre la partie dans la base de données
    """
    conn, cur = connexionDB(fichierDB)
    cur.execute("""
        INSERT INTO Score(Level, ScoreDate, Points, Lines, PlayerID)
        VALUES(?, date(), ?, ?,
            (SELECT PlayerID FROM Player WHERE Pseudo = ?))
    """, (niveau, points, lignes, pseudo))
    deconnexionDB(conn, cur)
