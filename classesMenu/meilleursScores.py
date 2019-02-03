# -*- coding: utf-8 -*-

##########################
#Meilleurs scores du jeu #
##########################

from tkinter import *
from tkinter.messagebox import *

from classesModifiees import FenetrePetite

import sys
sys.path.insert(0, "..")

from requetes import *
from constantes import *

class MeilleursScores(FenetrePetite):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        FenetrePetite.__init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments)

        reqTopDix = """SELECT Pseudo, Points, Lines
                        FROM Score, Player
                        WHERE Score.PlayerID = Player.PlayerID
                        ORDER BY Points Desc, Lines Desc
                        LIMIT 10"""

        reqTopDixPerso = """SELECT Pseudo, Points, Lines
                            FROM Score, Player
                            WHERE Score.PlayerID = Player.PlayerID
                            AND Player.Pseudo = '{}'
                            ORDER BY Points Desc, Lines Desc
                            LIMIT 10""".format(nomJoueur(fichierJoueur))

        conn, cur = connexionDB(fichierDB)
        self.scores = executeurDeRequetes(cur, [reqTopDix], 2)
        self.scoresPerso = executeurDeRequetes(cur, [reqTopDixPerso], 2)
        deconnexionDB(conn, cur)

        Label(self, text="Joueur", font=('Helvetica', 10)).grid(row=2, column=1)
        Label(self, text="Score@Lignes", font=('Helvetica', 10)).grid(row=2, column=2)

        self.perso = False
        self.majScores()

        self.bind('<Return>', self.majScores)

        if nomJoueur(fichierJoueur) != None:
            showinfo("Info pratique", "La touche entrée permet de switcher entre vos scores et ceux des autres :)")

    def majScores(self, event=None):
        ligneTab = 3

        for a in range(3, 13):
            Label(self, text="----------", font=('Helvetica', 8)).grid(row=a, column=1)
            Label(self, text="-----@-----", font=('Helvetica', 8)).grid(row=a, column=2)

        a = 3

        if not self.perso and nomJoueur(fichierJoueur) != None:
            scoresAffiche = self.scoresPerso
            self.perso = True

        else:
            scoresAffiche = self.scores
            self.perso = False

        for score in scoresAffiche:
            if score[0] == nomJoueur(fichierJoueur):
                score[0] = "MOI"

            Label(self, text="{}".format(score[0]), font=('Helvetica', 8)).grid(row=ligneTab, column=1)
            Label(self, text="{}@{}".format(score[1], score[2]), font=('Helvetica', 8)).grid(row=ligneTab, column=2)

            ligneTab += 1
